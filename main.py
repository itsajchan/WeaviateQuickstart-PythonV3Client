
import weaviate
from weaviate.embedded import EmbeddedOptions
from dotenv import load_dotenv
import requests
import json
import os


load_dotenv()

client = weaviate.Client(
    embedded_options=EmbeddedOptions(
        additional_env_vars={
        "ENABLE_MODULES":
        "text2vec-openai,generative-openai,qna-openai"}
    ),
    additional_headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

user_input = input("\n\n\nCreated a new Embedded Weaviate instance. If you want to delete any previous schema called \"Question\", type DELETE and press enter. Otherwise, press enter to continue to schema creation...")

if user_input == "DELETE":
    client.schema.delete_class("Question")
    input("\n\n\nDeleted previous schema called Question. Press enter to create a new schema...")

class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-openai",  
    "moduleConfig": {
        "text2vec-openai": {},
        "generative-openai": {}
    }
}
client.schema.create_class(class_obj)

print(f"The schema looks like this:\n\n{class_obj}")
input("\n\n\nCreated a new class called Question in Weaviate. Press enter to continue...")


resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
data = json.loads(resp.text)  # Load data

client.batch.configure(batch_size=100)  # Configure batch
with client.batch as batch:  # Initialize a batch process
    for i, d in enumerate(data):  # Batch import data
        print(f"importing question: {i+1}")
        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }
        batch.add_data_object(
            data_object=properties,
            class_name="Question"
        )

input("\n\n\nImported data. Press enter to continue...")

response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_limit(2)
    .do()
)

input("\n\n\nQueried Weaviate for questions related to biology. Press enter to see the results.\n\n\n")
print(json.dumps(response, indent=4))