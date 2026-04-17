"""
PDF processing utilities for legal document extraction
"""
import PyPDF2
from typing import List, Optional


def extract_pdf_text(pdf_path: str) -> str:
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text from the PDF
        
    Raises:
        Exception: If PDF is encrypted or cannot be read
    """
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Check if PDF is encrypted
            if pdf_reader.is_encrypted:
                raise Exception("PDF is encrypted. Please provide an unencrypted PDF.")
            
            # Extract text from all pages
            for page_num, page in enumerate(pdf_reader.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n--- Page {page_num + 1} ---\n{page_text}"
                except Exception as e:
                    raise Exception(f"Error extracting text from page {page_num + 1}: {str(e)}")
        
        if not text.strip():
            raise Exception("No text could be extracted. Document may be scanned or corrupted.")
        
        return text
        
    except FileNotFoundError:
        raise Exception(f"PDF file not found: {pdf_path}")
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")


def clean_text(text: str) -> str:
    """
    Clean extracted text.
    
    Args:
        text: Raw extracted text
        
    Returns:
        Cleaned text with normalized whitespace
    """
    # Normalize whitespace so the text is easier to process later.
    # This removes extra spaces, newlines, and tabs, and joins tokens with single spaces.
    text = ' '.join(text.split())
    return text


def process_document(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """
    Split document text into chunks.
    
    Args:
        text: Document text
        chunk_size: Size of each chunk
        overlap: Overlap between chunks
        
    Returns:
        List of text chunks
    """
    chunks = []
    step = chunk_size - overlap
    
    for i in range(0, len(text), step):
        """ from i to i + chunk_size, with an overlap of 'overlap' characters """
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks


def get_document_stats(text: str) -> dict:
    """
    Get statistics about the document.
    
    Args:
        text: Document text
        
    Returns:
        Dictionary with document statistics
    """
    words = text.split()
    sentences = text.split('.')
    
    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "character_count": len(text),
        "average_word_length": sum(len(w) for w in words) / len(words) if words else 0
    }
