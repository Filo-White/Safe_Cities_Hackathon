import openai  
import os  
import fitz  

#For RDF handling
from rdflib import Graph

# To prevent asyncio-related issues in environments like Jupyter Notebook:
import nest_asyncio

# GUI handling for file selection dialogs:
import tkinter as tk
from tkinter import filedialog

#For private info upload
from dotenv import load_dotenv

# For Llama index functionalities
from llama_parse import LlamaParse  
from llama_index.core import Document, VectorStoreIndex, PropertyGraphIndex
from llama_index.core.node_parser import MarkdownElementNodeParser 
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import PropertyGraphIndex
from llama_index.core.indices.property_graph import SchemaLLMPathExtractor
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore

nest_asyncio.apply()

# CONFIGURATION
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llama_api_key = os.getenv("LLAMA_API_KEY")

os.environ["NEO4J_URI"] = os.getenv("NEO4J_URI")
os.environ["NEO4J_USERNAME"] = os.getenv("NEO4J_USERNAME")
os.environ["NEO4J_PASSWORD"] = os.getenv("NEO4J_PASSWORD")

if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    print("OpenAI API key loaded successfully.")
else:
    print("OpenAI API key not found in .env file.")

if llama_api_key:
    os.environ["LLAMA_API_KEY"] = llama_api_key
    print("Llama API key loaded successfully.")
else:
    print("Llama API key not found in .env file.")


URI = os.getenv("NEO4J_URI")  # Neo4j connection URI (e.g., bolt://localhost:7687)
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))  # Username and password tuple

# Establish connection to the Neo4j database and verify connectivity
with GraphDatabase.driver(URI, auth=AUTH) as driver:
    try:
        driver.verify_connectivity()  # Verifies the connection to the database
        print("Connection established successfully.")
    except Exception as e:
        print(f"Failed to establish connection: {e}")


# select your file from your computer
def select_file():
    root = tk.Tk()  
    root.withdraw()  
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("File OWL, PDF, TXT e CSV", "*.owl *.pdf *.txt *.csv"), ("All files", "*.*"))
    )
    return file_path

selected_file = select_file()
if selected_file:
    print(f"You selected: {selected_file}")
else:
    print("None file selected")

from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore


# GRAPH CONFIGURATION
graph_store = Neo4jPropertyGraphStore(
    username=os.environ["NEO4J_USERNAME"], 
    password=os.environ["NEO4J_PASSWORD"], 
    url=os.getenv("NEO4J_URI")
)

# PARSING 
parser = LlamaParse(
    api_key = llama_api_key,
    result_type="markdown" # other options json, text, html, raw 
)

documents = await parser.aload_data(selected_file)

# INDEXING 
index = PropertyGraphIndex.from_documents(
    documents,
    embed_model=OpenAIEmbedding(model_name="text-embedding-3-small"),
    property_graph_store=graph_store,
    show_progress=True,
)

