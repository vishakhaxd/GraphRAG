
import os
import networkx as nx
from pyvis.network import Network
from llama_index.core import SimpleDirectoryReader, KnowledgeGraphIndex, Settings
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.llms.openai import OpenAI

from config import settings  # local config

# Initialise global LlamaIndex settings
Settings.llm = OpenAI(model=settings.MODEL, temperature=0)
Settings.graph_store = SimpleGraphStore()

def _load_document(file_path: str):
    """Load a single document with SimpleDirectoryReader."""
    reader = SimpleDirectoryReader(input_files=[file_path])
    return reader.load_data()

def build_knowledge_graph(file_path: str) -> nx.Graph:
    """Build a NetworkX graph from the document."""
    os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
    documents = _load_document(file_path)
    index = KnowledgeGraphIndex.from_documents(
        documents,
        max_triplets_per_chunk=10,
    )
    return index.get_networkx_graph()

def visualize_graph(graph: nx.Graph, output_path: str):
    """Render the graph to an interactive HTML file via PyVis."""
    net = Network(height="750px", width="100%", notebook=False)
    net.from_nx(graph)
    net.show(output_path)
    return output_path
