# Safe Cities Hackathon
![ciao](https://github.com/Filo-White/Safe_Cities_Hackathon/blob/main/image/Screenshot%202025-01-11%20175708.png)

This repository contains our project submission for the SafeCities Hackathon, part of the SummerSOC2024 event. Our work focuses on leveraging Knowledge Graphs (KG) and Large Language Models (LLMs) to tackle challenges related to the Safe Cities Security Vulnerability Assessment (SVA) framework.

## Overview

To address the hackathon challenge, we developed two core algorithms:

**1. Automatic Knowledge Graph Extraction**

This algorithm enables the automated extraction of a Knowledge Graph (KG) from structured and unstructured data sources, including:

* PDF documents
* TXT files
* CSV datasets

The extracted entities, relationships, and contextual information are automatically ingested into a Neo4j database, streamlining the creation of domain-specific KGs. This process significantly reduces the manual effort required to build a KG from diverse data formats, ensuring scalability and accuracy.

**2. Retrieval-Augmented Generation (RAG) using Knowledge Graphs**

The second algorithm integrates the extracted KG with a Retrieval-Augmented Generation (RAG) pipeline, enabling Large Language Models (LLMs) to:
* Retrieve accurate and relevant information from the KG.
* Answer domain-specific questions related to the Safe Cities SVA framework.

This integration ensures that the LLM’s responses are:

* Contextually grounded in the KG’s data.
* Precise and aligned with the specific requirements of security vulnerability assessment.

## Use Case: Safe Cities SVA Framework

Our solution is tailored to assist in analyzing and assessing security vulnerabilities in urban environments. By combining automatic KG extraction and RAG-based LLM capabilities, we provide a robust tool for:

* Extracting and organizing relevant data for the SVA framework.
* Facilitating accurate decision-making and knowledge dissemination.

## Implementation Details

Technologies Used:

* Neo4j for Knowledge Graph storage and querying.
* Custom parsing algorithms for PDF, TXT, and CSV files.
* OpenAI GPT-based models for RAG implementation.

## Workflow:

Input data (PDF/TXT/CSV) is processed by the KG extraction algorithm. Extracted data is ingested into Neo4j, forming the domain-specific KG. The KG is integrated with the RAG pipeline, enabling the LLM to provide accurate responses based on the extracted knowledge.

## Results

Our approach demonstrates significant improvements in:
* automating the creation of Knowledge Graphs from heterogeneous data sources.
* enhancing the accuracy and contextual relevance of LLM-generated responses in the Safe Cities domain.

# Getting Started
This guide will help you set up Martialis and run your first tasks for question answering and text generation.

## Installation
First of all, clone the repository:


```bash
git clone https://github.com/Filo-White/Safe_Cities_Hackathon.git
```

```bash
cd src
```

Before starting, ensure you have the required libraries listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Configuration
After cloning the repository, you need to configure the `.env` file with the correct values for your environment. Follow these steps: 

1. copy the file `.env.sample` as file `.env` using the following command
```bash
cp .env.sample .env
```

2. Update variables in the `.env` file:
 * `OPEN_API_KEY`: your openai key
 * `LLAMA_API_KEY`: your llama key
 * `NEO4J_USERNAME`: username of neo4j DB
 * `NEO4J_PASSWORD`: password for ne4j DB
 * `NEO4J_URL`: URL of neo4j DB



 # Documentation
For more detailed information on the underlying concepts and methodologies that Martialis is based on, please refer to the following papers:

1. **Bianchini F., Calamo M., De Luzi F., Macrì M and Mecella M. (2024)** - [*Enhancing Complex Linguistic Tasks Resolution through Fine-tuning LLMs, RAG, and Knowledge Graphs*](https://doi.org/10.1007/978-3-031-61003-5_13)
   This paper introduces the integration of Knowledge Graphs into the RAG framework to solve complex linguistic tasks in domain-specific contexts. It lays the foundation for the approach used in Martialis, focusing on improving LLM capabilities by incorporating structured knowledge.

2. **Bianchini F., Calamo M., De Luzi F., Macrì M and Mecella M. (2024)** - [*A Service-Based Pipeline for Complex Linguistic Tasks Adopting LLMs and Knowledge Graphs*](https://doi.org/10.1007/978-3-031-72578-4_8)  
   This work presents a service-based framework that adapts LLMs and Knowledge Graphs to provide precise answers and domain-specific text generation. It discusses the modular architecture and the potential for applying Martialis across various industries, including healthcare and law.
