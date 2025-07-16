# Knowledge Graph App

Generate, visualize, and query knowledge graphs from documents using LlamaIndex, FastAPI, and PyVis.

![Sample Knowledge Graph](docs/sample_knowledge_graph.png)

> The full interactive knowledge graph is located at [`notebooks/graph_demo.html`](notebooks/graph_demo.html).

## Overview

This project extracts structured knowledge from unstructured text (e.g., research papers), visualizes it as an interactive knowledge graph, and enables querying of entities and relationships. It leverages LlamaIndex for knowledge extraction and querying, OpenAI LLMs for language understanding, and PyVis for graph visualization. The backend is built with FastAPI.

## Features
- Upload a text document and automatically generate a knowledge graph
- Interactive HTML visualization of entities and relationships
- Query the knowledge graph for entities, relationships, and facts
- Uses OpenAI LLMs for semantic understanding
- Extensible for different document types and domains

## Project Structure
```
backend/        # FastAPI backend and graph building logic
  app.py        # API endpoints
  graph_builder.py # Knowledge graph construction, visualization, and querying
  config.py     # Configuration and environment variables
  __init__.py
frontend/       # (Placeholder for frontend code)
data/           # Example input documents (e.g., ai_papers.txt)
notebooks/      # Jupyter notebooks and HTML graph demos
outputs/        # Generated HTML graph visualizations
pyproject.toml  # Poetry dependencies
```

## Setup

### Prerequisites
- Python 3.10+
- [Poetry](https://python-poetry.org/docs/)
- OpenAI API key (for LlamaIndex/OpenAI integration)

### Installation
```sh
# Clone the repository
$ git clone <repo-url>
$ cd GraphRAG

# Install dependencies
$ poetry install

# Set up environment variables
$ cp backend/.env.example backend/.env
# Edit backend/.env and add your OPENAI_API_KEY
```

### Running the Backend
```sh
$ poetry run uvicorn backend.app:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

### Example Usage
- Place a text file (e.g., `ai_papers.txt`) in the `data/` directory.
- Use the `/upload/` endpoint to upload a file and generate a knowledge graph.
- The resulting HTML visualization will be saved in the `outputs/` directory.
- Query the knowledge graph using the API or Jupyter notebook (see below).

### Querying the Knowledge Graph
You can query the knowledge graph for entities, relationships, and facts using LlamaIndex in a Jupyter notebook:

```python
query_engine = index.as_query_engine(include_text=True)
response = query_engine.query("List the people in this document.")
print(response)
```

See `notebooks/knowledge_graph_demo.ipynb` for more interactive querying examples.

### Jupyter Notebook Demo
See `notebooks/knowledge_graph_demo.ipynb` for an interactive demo of the knowledge graph pipeline and querying.

## Configuration
- Edit `backend/config.py` or use a `.env` file to set your OpenAI API key and model.

## Dependencies
- llama-index
- openai
- fastapi
- uvicorn
- pyvis
- networkx
- python-dotenv

## License
MIT

---

*This project is a template for building knowledge graph applications from unstructured text using modern LLMs and visualization tools.*
