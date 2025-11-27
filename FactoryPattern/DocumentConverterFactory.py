from Document import Document, PlainTextDocument, MarkdownDocument

class DocumentConverterFactory:
    @staticmethod
    def create_converter(file_path: str) -> Document:
        """
        Factory method to create a Document converter based on file extension.
        Supports .txt for PlainTextDocument and .md for MarkdownDocument.
        """
        if file_path.endswith('.txt'):
            return PlainTextDocument()
        elif file_path.endswith('.md'):
            return MarkdownDocument()
        else:
            raise ValueError(f"Unsupported file format for file: {file_path}")