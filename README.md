# Weaviate Quickstart in Embedded Mode with Python V3 Client

![GIF of Weaviate in Action](WeaviateQuickstart.gif)

## Python Weaviate Client with Data Import and Query
This script is a Python example for Weaviate, an open-source vector database. It uses the weaviate Python package to interact with an embedded Weaviate instance, import data, and perform a query.

## Environment Setup
The script begins by importing necessary modules and loading environment variables using dotenv. The OPENAI_API_KEY is expected to be in the environment variables which you can get from https://openai.com/. 

## Weaviate Client Initialization
A Weaviate client is initialized with embedded options and additional headers. The embedded options enable three modules: text2vec-openai, generative-openai, and qna-openai, but there are many more you can choose from the [Weaviate Docs](https://weaviate.io/developers/weaviate/configuration/modules). The X-OpenAI-Api-Key is passed in the headers.

## User Input
The script then prompts the user for input. When prompted for a deletion, if the user types "DELETE", the script will delete any existing schema named "Question" from the Embeddded Weaviate instance.

## Schema Creation
A new schema named "Question" is created with the vectorizer set to text2vec-openai and module configurations for text2vec-openai and generative-openai.

## Data Import
The script fetches a JSON file from a URL and loads the data. It then configures a batch process and imports the data into the "Question" schema in the Weaviate instance.

## Query - Basic Semantic Search
The script performs a query on the "Question" schema for questions related to "biology" and prints the results to the console.

## Usage
Set the OPENAI_API_KEY environment variable.
Set up a python virtual environment and install the dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the script: `python main.py`

Follow the prompts to understand what's going on in real time!

## Next Steps
This is an example of using Weaviate for semantic search, it's based off the Quickstart available in the Weaviate Docs. There are many other types of search available through Weaviate. Check them out at https://weaviate.io/

Explore the [Weaviate documentation](https://weaviate.io/developers/weaviate) for more information on its features and capabilities.