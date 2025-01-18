from read_article_pdf import pdf_read_by
from read_article_ocr import ocr_read_by

def read_by(articles):
    for article in articles:
        for numberAndLink in article["number_and_link"]:
            # Mais que 2000  
            if int(article["year"]) > 2000:
                print("PDF {}/{}".format(article["year"], numberAndLink["number"]))
                pdf_read_by(numberAndLink["link"])
                continue
                
            # Menos que 2000
            if int(article["year"]) < 2000:
                print("OCR {}/{}".format(article["year"], numberAndLink["number"]))
                ocr_read_by(numberAndLink["link"])
                continue

            # Anos 2000, se o numero for maior que 4 usa PDF, caso contrário usa OCR
            if int(numberAndLink["number"]) > 4:
                print("PDF {}/{}".format(article["year"], numberAndLink["number"]))
                pdf_read_by(numberAndLink["link"])
                continue
            else:
                print("OCR {}/{}".format(article["year"], numberAndLink["number"]))
                ocr_read_by(numberAndLink["link"])
                continue
            
