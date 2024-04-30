import streamlit as st
from src.word_embedding_visualizer import WordEmbeddingVisualizer

def main():
    st.title("Word Embedding Visualization")
    
    # Load CSS styles
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    # Container for inputs
    with st.container():
        st.header("Input Settings")
        
        # Select model
        model = st.selectbox("Select Model", ["en_core_web_md"], 
                             help="Choose the word embedding model.")

        # Select dimensionality reduction technique
        technique = st.selectbox("Select Dimensionality Reduction Technique", ["PCA", "UMAP", "TSNE"],
                                 help="Choose the dimensionality reduction technique.")
        
        # Select 2D or 3D visualization
        dimensions = st.selectbox("Select Dimensionality (2D or 3D)", [2, 3],
                                  help="Choose 2D or 3D visualization.")
        
        # Text input for user-supplied text
        user_text = st.text_input("Enter your own text:", 
                                  help="Enter the text you want to visualize.")

        # Visualize button
        if st.button("Visualize", key="visualize_button"):
            if user_text:
                words, vecs = WordEmbeddingVisualizer(model, technique, dimensions).process_user_text(user_text)

                # Create WordEmbeddingVisualizer instance and visualize
                visualizer = WordEmbeddingVisualizer(model, technique, dimensions)
                visualizer.visualize(words, vecs)
            else:
                st.warning("Please supply the input_text")
                
if __name__ == "__main__":
    main()
