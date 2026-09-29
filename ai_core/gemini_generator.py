import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


class GeminiDocumentGenerator:
    """Generates legal documents using Google Gemini."""

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-3.8-flash"

    def generate_document(self, document_type, parties, terms, dates):
        """Generate a legal document based on the user's input."""
        prompt = f"""You are a professional legal assistant. Generate a comprehensive legal document.

Document Type: {document_type}
Involved Parties: {parties}
Effective Date: {dates}
Terms and Conditions: {terms}

Requirements:
- Use formal legal language and structure.
- Include a clear title at the top.
- Structure the document with numbered sections (1. Services, 2. Term, 3. Payment, etc.).
- Include clauses for confidentiality, governing law, and signature blocks.
- Do NOT use markdown symbols like ** or #.
- Format the response as plain text with proper line breaks between sections."""

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            return f"Error generating document: {str(e)}"