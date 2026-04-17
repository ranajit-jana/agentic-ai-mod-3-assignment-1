"""
Main Streamlit application for Legal Document Review
"""
import os
import sys
from pathlib import Path
import streamlit as st

# Add the src directory to Python's import search path.
# This allows importing modules located inside src/ (like utils and rag_pipeline)
# even though the app is running from the project root.
sys.path.insert(0, str(Path(__file__).parent / "src"))

from utils import extract_pdf_text, process_document
from rag_pipeline import RAGPipeline
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP, RETRIEVAL_K

# Page configuration
st.set_page_config(
    page_title="Legal Document Review",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f4788;
        margin-bottom: 1rem;
    }
    .subheader {
        color: #4a6fa5;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "rag_pipeline" not in st.session_state:
    st.session_state.rag_pipeline = None
if "document_loaded" not in st.session_state:
    st.session_state.document_loaded = False
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = None

# Sidebar
st.sidebar.markdown("## ⚖️ Configuration")

# Load API key from .env file
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.sidebar.error("❌ GOOGLE_API_KEY not found in .env file")
    st.sidebar.info("Please create a .env file with your Google Gemini API key")
    st.stop()
else:
    st.sidebar.success("✅ API key loaded from .env file")

st.sidebar.markdown("---")
st.sidebar.markdown("### Settings")
chunk_size = st.sidebar.slider(
    "Chunk Size",
    min_value=500,
    max_value=2000,
    value=CHUNK_SIZE,
    step=100,
    help="Size of text chunks for embedding"
)

chunk_overlap = st.sidebar.slider(
    "Chunk Overlap",
    min_value=0,
    max_value=500,
    value=CHUNK_OVERLAP,
    step=50,
    help="Overlap between chunks for context preservation"
)

retrieval_k = st.sidebar.slider(
    "Number of Retrieved Chunks",
    min_value=1,
    max_value=10,
    value=RETRIEVAL_K,
    help="Number of chunks to retrieve for context"
)

st.sidebar.markdown("---")
st.sidebar.info(
    "📄 Upload a legal PDF document to begin. The app will extract text, "
    "generate embeddings, and enable semantic search."
)

# Main content
st.markdown('<h1 class="main-header">⚖️ Legal Document Review Application</h1>', unsafe_allow_html=True)
st.markdown(
    "Upload a legal document and leverage AI to summarize, analyze, and answer questions about its content."
)

st.markdown('<h2 class="subheader">📄 Document Upload</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Upload a PDF document",
        type="pdf",
        help="Select a text-based PDF document (not scanned)"
    )

with col2:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.document_loaded = False
        st.session_state.extracted_text = None
        st.session_state.rag_pipeline = None
        st.rerun()

# Process uploaded file
if uploaded_file and api_key:
    if not st.session_state.document_loaded:
        with st.spinner("🔄 Processing document..."):
            try:
                # Save uploaded file temporarily
                temp_pdf_path = f"temp_{uploaded_file.name}"
                with open(temp_pdf_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Extract text
                extracted_text = extract_pdf_text(temp_pdf_path)
                st.session_state.extracted_text = extracted_text
                
                # Initialize RAG pipeline
                st.session_state.rag_pipeline = RAGPipeline(
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                    retrieval_k=retrieval_k
                )
                
                # Process document
                st.session_state.rag_pipeline.process_document(extracted_text)
                st.session_state.document_loaded = True
                
                # Clean up temp file
                os.remove(temp_pdf_path)
                
                st.success("✅ Document processed successfully!")
                
            except Exception as e:
                st.error(f"❌ Error processing document: {str(e)}")

# Display document preview
if st.session_state.document_loaded and st.session_state.extracted_text:
    st.markdown('<h2 class="subheader">👁️ Document Preview</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col2:
        if st.button("📋 Show Full Text"):
            with st.expander("Full Document Text"):
                st.text_area(
                    "Extracted Text",
                    value=st.session_state.extracted_text[:3000] + "..." if len(st.session_state.extracted_text) > 3000 else st.session_state.extracted_text,
                    height=300,
                    disabled=True
                )
    
    # Document statistics
    word_count = len(st.session_state.extracted_text.split())
    st.metric("Document Statistics", f"{word_count} words")

# Q&A Section
if st.session_state.document_loaded:
    st.markdown('<h2 class="subheader">❓ Ask Questions</h2>', unsafe_allow_html=True)
    
    question = st.text_input(
        "Enter your question about the document:",
        placeholder="e.g., What are the termination clauses?",
        help="Ask any question about the document content"
    )
    
    if st.button("Get Answer", type="primary", use_container_width=True):
        if question.strip():
            with st.spinner("🔍 Searching document and generating answer..."):
                try:
                    answer = st.session_state.rag_pipeline.answer_question(question)
                    st.markdown("### 📝 Answer:")
                    st.write(answer)
                except Exception as e:
                    st.error(f"❌ Error generating answer: {str(e)}")
        else:
            st.warning("⚠️ Please enter a question")

# Summarization Section
if st.session_state.document_loaded:
    st.markdown('<h2 class="subheader">📊 Document Summary</h2>', unsafe_allow_html=True)
    
    if st.button("Generate Summary", type="primary", use_container_width=True):
        with st.spinner("📝 Generating summary..."):
            try:
                summary = st.session_state.rag_pipeline.summarize_document()
                st.markdown("### Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"❌ Error generating summary: {str(e)}")

# Instructions
if not st.session_state.document_loaded:
    st.markdown("---")
    st.info(
        """
        ### 🚀 Getting Started:
        1. **Enter API Key**: Provide your Google Gemini API key in the sidebar
        2. **Upload Document**: Select a PDF legal document
        3. **Ask Questions**: Query the document using natural language
        4. **Get Summary**: Generate a concise summary of key points
        
        ### Examples of questions you can ask:
        - What are the main terms and conditions?
        - What are the payment obligations?
        - When does this contract expire?
        - What are the termination clauses?
        """
    )

st.markdown("---")
st.markdown(
    "<small>⚖️ Legal Document Review Application | "
    "Powered by LangChain & Google Gemini | "
    "Assignment: Agentic AI Module 3</small>",
    unsafe_allow_html=True
)
