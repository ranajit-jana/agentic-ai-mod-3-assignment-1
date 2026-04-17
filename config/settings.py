"""
Configuration and settings for the Legal Document Review application
"""

# Text processing settings
CHUNK_SIZE = 1000  # Size of each text chunk in characters
CHUNK_OVERLAP = 200  # Overlap between chunks in characters

# RAG settings
RETRIEVAL_K = 3  # Number of chunks to retrieve for context
MAX_CONTEXT_LENGTH = 4000  # Maximum context length for the LLM

# Model settings
LLM_MODEL = "gemini-1.5-flash"  # Google Gemini model to use
EMBEDDINGS_MODEL = "models/embedding-001"  # Embeddings model
TEMPERATURE = 0.7  # LLM temperature (0-1, higher = more creative)

# File settings
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB max file size
ALLOWED_EXTENSIONS = ['.pdf']  # Allowed file extensions
TEMP_DIR = "temp"  # Temporary directory for uploads

# Streamlit settings
PAGE_TITLE = "⚖️ Legal Document Review"
PAGE_ICON = "📄"
LAYOUT = "wide"

# Prompt templates
LEGAL_QA_SYSTEM_PROMPT = """
You are an expert legal assistant specializing in document analysis and review.
Your role is to help legal professionals understand, summarize, and extract information from legal documents.

When answering questions:
- Be precise and cite relevant sections
- Distinguish between mandatory and optional terms
- Flag potential risks or ambiguities
- Explain legal terminology clearly
- Maintain professional and objective tone
"""

SUMMARIZATION_SYSTEM_PROMPT = """
You are an expert legal document analyst. Create clear, concise summaries that capture:
- Main contract type and parties
- Key obligations and responsibilities
- Important dates and deadlines
- Payment terms and conditions
- Termination and renewal clauses
- Liability and indemnification
- Confidentiality provisions
- Any unusual or potentially problematic clauses

Format the summary in a structured, easy-to-read manner.
"""
