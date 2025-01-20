from pathlib import Path
from docling.document_converter import DocumentConverter

def pdf_to_md_by(file_path):
    input_doc = Path(file_path)

    converter = DocumentConverter()
    result = converter.convert(input_doc)
    md = result.document.export_to_markdown()
    
    # Define o caminho para salvar o arquivo .md
    output_file = input_doc.with_suffix("_original.md")  # Altera a extensão para .md
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(md)
    
    print(f"Arquivo Markdown salvo em: {output_file}")