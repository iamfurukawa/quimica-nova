from pathlib import Path
from docling.document_converter import DocumentConverter

def simple_read_by(file_path):
    input_doc = Path(file_path)

    converter = DocumentConverter()
    result = converter.convert(input_doc)
    print(result.document.export_to_markdown())
