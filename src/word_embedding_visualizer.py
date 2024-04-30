import numpy as np
from sklearn.decomposition import PCA
import umap
import streamlit as st
from sklearn.manifold import TSNE
import spacy
import plotly.express as px
from typing import List, Tuple


class WordEmbeddingVisualizer:
    def __init__(self, model_name: str, technique: str, dimensions: int):
        self.model_name = model_name
        self.technique = technique
        self.dimensions = dimensions
        self.nlp = spacy.load(self.model_name)

    def _reduce_dimensionality(self, vecs: np.ndarray) -> np.ndarray:
        if self.technique == "PCA":
            reducer = PCA(n_components=self.dimensions)
        elif self.technique == "UMAP":
            reducer = umap.UMAP(n_components=self.dimensions)
        elif self.technique == "TSNE":
            reducer = TSNE(n_components=self.dimensions, perplexity=min(vecs.shape)-1)
        else:
            raise ValueError("Invalid dimensionality reduction technique selected.")
        return reducer.fit_transform(vecs)

    def visualize(self, words: List[str], vecs: np.ndarray) -> None:
        vecs_transformed = self._reduce_dimensionality(vecs)
        if self.dimensions == 2:
            fig = px.scatter(x=vecs_transformed[:, 0], y=vecs_transformed[:, 1], text=words, title="Word Embedding Visualization")
        elif self.dimensions == 3:
            fig = px.scatter_3d(x=vecs_transformed[:, 0], y=vecs_transformed[:, 1], z=vecs_transformed[:, 2], text=words, title="Word Embedding Visualization")
        else:
            raise ValueError("Invalid dimensionality selected.")
        fig.update_traces(textposition='top center')
        st.plotly_chart(fig)

    def process_user_text(self, user_text: str) -> Tuple[List[str], np.ndarray]:
        doc = self.nlp(user_text)
        words = [token.text for token in doc if token.has_vector]
        vecs = np.array([token.vector for token in doc if token.has_vector])
        return words, vecs
