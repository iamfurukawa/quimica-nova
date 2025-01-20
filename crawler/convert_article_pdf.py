from pathlib import Path
from docling.document_converter import DocumentConverter

def pdf_to_md_by(file_path):
    input_doc = Path(file_path)

    output_file = input_doc.with_name(input_doc.stem + "_original.md")
    
    # Verifica se o arquivo .md já existe
    if output_file.exists():
        print(f"O arquivo Markdown já existe: {output_file}")
        return  # Se o arquivo já existe, não reprocessa

    converter = DocumentConverter()
    result = converter.convert(input_doc)
    md = result.document.export_to_markdown()
    
    # Define o caminho para salvar o arquivo .md
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(md)
    
    print(f"Arquivo Markdown salvo em: {output_file}")