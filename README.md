# Safe Cities Hackathon

# Getting Started
This guide will help you set up Martialis and run your first tasks for question answering and text generation.

## Installation
First of all, clone the repository:


```bash
git clone https://github.com/DIAG-Sapienza-BPM-Smart-Spaces/Martialis.git
```

```bash
cd Martialis
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
 * `OPEN_API_KEY`: 
 * `NEO4J_USERNAME`:
 * `NEO4J_PASSWORD`:
 * `NEO4J_URL`:
 * `DOCUMENT_PATH (optional)`:
 * `ONTOLOGY_PATH (optional)`: 
