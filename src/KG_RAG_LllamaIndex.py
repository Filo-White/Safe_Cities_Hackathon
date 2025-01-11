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


nest_asyncio.apply()

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llama_api_key = os.getenv("LLAMA_API_KEY")

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


parser = LlamaParse(
    api_key = os.environ["LLAMA_API_KEY"],
    result_type="markdown" # other options json, text, html, raw 
)

documents = await parser.aload_data(selected_file)
print(f"Document parsing for {selected_file}: COMPLETED")

index = PropertyGraphIndex.from_documents(documents)
print(f"Indexing of document {selected_file}: COMPLETED")

query_engine = index.as_query_engine(
    llm = OpenAI(model="gpt-4-turbo"),
    response_mode = "compact",
    include_text=True,  
    similarity_top_k=2,  
    verbose=True,
)

# Insert you query 
user_query = input("Enter your query: ")

# Execute a query and retrieve the response
response = query_engine.query(user_query)
print(f"Answer: {response}")
