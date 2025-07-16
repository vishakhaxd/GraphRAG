
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from graph_builder import build_knowledge_graph, visualize_graph
import shutil
import os
import uuid

app = FastAPI(title="Knowledge Graph Backend")

# Enable CORS for any origin (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Upload a document, build a knowledge graph, and return the HTML path."""
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Build and visualize graph
    graph = build_knowledge_graph(file_path)
    html_name = f"{file_id}_graph.html"
    html_path = os.path.join(OUTPUT_DIR, html_name)
    visualize_graph(graph, output_path=html_path)

    # Return relative path for frontend
    relative_path = f"outputs/{html_name}"
    return {"message": "File processed", "graph_html": relative_path}
