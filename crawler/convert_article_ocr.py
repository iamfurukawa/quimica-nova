from pathlib import Path
from docling.backend.docling_parse_backend import DoclingParseDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    TesseractCliOcrOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption

def ocr_to_md_by(file_path):
    input_doc = Path(file_path)

    output_file = input_doc.with_name(input_doc.stem + "_original.md")
    
    # Verifica se o arquivo .md já existe
    if output_file.exists():
        print(f"O arquivo Markdown já existe: {output_file}")
        return  # Se o arquivo já existe, não reprocessa

    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True

    ocr_options = TesseractCliOcrOptions(force_full_page_ocr=True)
    pipeline_options.ocr_options = ocr_options

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options,
            )
        }
    )

    doc = converter.convert(input_doc).document
    md = doc.export_to_markdown()

    # Define o caminho para salvar o arquivo .md
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(md)
    
    print(f"Arquivo Markdown salvo em: {output_file}")