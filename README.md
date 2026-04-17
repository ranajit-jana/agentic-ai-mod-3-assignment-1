# Legal Document Review Application with LangChain

A modern web-based application that leverages AI and Retrieval-Augmented Generation (RAG) to help legal professionals efficiently review, summarize, and query complex legal documents.

## Features

- **PDF Upload & Processing**: Extract text from legal PDF documents with error handling for encrypted/scanned files
- **Semantic Search**: Embed document chunks using Google Gemini embeddings and store in FAISS for fast retrieval
- **RAG-Based Q&A**: Answer document-specific questions using context-aware LLM responses
- **Document Summarization**: Generate concise summaries of uploaded legal documents
- **Secure API Management**: Safely manage API keys through environment variables
- **User-Friendly Interface**: Built with Streamlit for intuitive interactions

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python with LangChain
- **LLM**: Google Gemini 1.5 Flash
- **Embeddings**: Google Gemini Embeddings
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **PDF Processing**: PyPDF2
- **Text Chunking**: LangChain's RecursiveCharacterTextSplitter

## Project Structure

```
agentic-ai-mod-3-assignment-1/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
├── src/
│   ├── utils.py               # PDF extraction and text processing utilities
│   ├── rag_pipeline.py        # RAG pipeline implementation
│   └── __init__.py
├── config/
│   ├── settings.py            # Configuration and constants
│   └── __init__.py
└── data/
    └── sample_documents/      # Directory for storing uploaded/sample PDFs
```

## Prerequisites

- Python 3.9+
- pip package manager
- Google Gemini API key (free tier available at [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ranajit-jana/agentic-ai-mod-3-assignment-1.git
   cd agentic-ai-mod-3-assignment-1
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**:
   Open your browser and navigate to `http://localhost:8501`

3. **Use the application**:
   - Enter your Google Gemini API key in the sidebar
   - Upload a legal PDF document
   - View extracted text and preview
   - Ask questions about the document
   - Get instant answers with relevant context
   - View document summary

## Key Features Explained

### PDF Text Extraction
- Supports text-based PDF documents
- Handles errors gracefully for scanned or encrypted PDFs
- Extracts full text with metadata preservation

### Text Chunking & Embedding
- Splits documents into manageable chunks using `RecursiveCharacterTextSplitter`
- Generates semantic embeddings using Google Gemini
- Stores embeddings in FAISS for efficient similarity search

### RAG Question Answering
- Retrieves relevant document chunks based on query similarity
- Passes context to Gemini 1.5 Flash for intelligent responses
- Provides source attribution for answers

### Document Summarization
- Analyzes key sections of the document
- Generates concise, legal-focused summaries
- Captures important clauses and obligations

## Configuration

Edit `config/settings.py` to customize:
- Chunk size and overlap
- Number of retrieved chunks for context
- Model parameters
- Temperature and other LLM settings

## Deployment

### Local Deployment
```bash
streamlit run app.py
```

### Community Cloud Deployment
1. Push your code to GitHub
2. Visit [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Deploy directly from your GitHub repository
4. Add secrets (API keys) through the cloud dashboard

## Sample Legal Documents

For testing, you can use:
- Free templates from [Legal Document Repositories](https://www.lawbox.com/)
- Sample contracts and NDAs (publicly available)
- Your own document PDFs

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "API key not found" | Ensure `GOOGLE_API_KEY` is set in `.env` file |
| PDF extraction fails | Verify PDF is text-based, not scanned |
| Slow embedding generation | Reduce chunk overlap or use smaller documents |
| FAISS index error | Ensure embeddings match vector dimensions |

## Future Enhancements

- [ ] Support for scanned PDFs using OCR
- [ ] Multi-document comparison
- [ ] Specific clause extraction
- [ ] Risk assessment scoring
- [ ] Document redaction capabilities
- [ ] Chat history persistence
- [ ] Export functionality (PDF, DOCX)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is provided as-is for educational purposes.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Author**: [Your Name]  
**Created**: 2026  
**Assignment**: Agentic AI Module 3 - Assignment 1
