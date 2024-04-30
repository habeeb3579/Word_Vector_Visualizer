# Word Vector Embedding Visualization with SpaCy, Streamlit and Docker

This project demonstrates how to visualize word embeddings using SpaCy, Streamlit and Docker. Word embeddings are numerical representations of words in a high-dimensional space, often used in natural language processing (NLP) tasks. With this application, you can visualize word embeddings in 2D or 3D space using techniques like PCA, UMAP, or t-SNE.

## Features

- Visualize word embeddings in 2D or 3D space.
- Select from different dimensionality reduction techniques: PCA, UMAP, t-SNE.
- Select a pre-trained word embedding model or supply your own text for visualization.
- Interactive plots with Streamlit and Plotly.
- Dockerized for easy deployment.

## Installation

1. Clone the repository:

        git clone https://github.com/habeeb3579/Word-Vector-Visualizer.git
2. Cd into the repo

        cd Word-Vector-Visualizer


## Usage
### Running Using Docker
Ensure you have Docker installed on your system.

Build the Docker image:

        docker build -t word-embedding-app:v1 .

        docker run -p 8501:8501 word-embedding-app

The application will be accessible at [http://localhost:8501](http://localhost:8501).


