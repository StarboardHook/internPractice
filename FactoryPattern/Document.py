from abc import ABC, abstractmethod

class Document(ABC):
    """
    Abstract base class for different document types.
    All document types should have a 'load' and 'process' method.
    """
    @abstractmethod
    def load(self, filepath: str):
        pass

    @abstractmethod
    def process(self) -> str:
        """
        Processes the loaded document and returns a standardized string representation.
        """
        pass

class PlainTextDocument(Document):
    """
    Represents a plain text document.
    """
    def __init__(self):
        self._content = ""

    def load(self, filepath: str):
        with open(filepath, 'r') as f:
            self._content = f.read()

    def process(self) -> str:
        return self._content.strip()

class MarkdownDocument(Document):
    """
    Represents a Markdown document (simplified for this exercise).
    """
    def __init__(self):
        self._content = ""

    def load(self, filepath: str):
        with open(filepath, 'r') as f:
            self._content = f.read()

    def process(self) -> str:
        # Simplified Markdown processing: just add a header indicator
        lines = [f"# {line.strip()}" if line.startswith("#") else line.strip() for line in self._content.splitlines()]
        return "\n".join(lines)
