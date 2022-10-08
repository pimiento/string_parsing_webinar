#!/usr/bin/env python3
import io

from pdfminer.converter import HTMLConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams

def extract_text_from_pdf(pdf_path):
    params = {
        "scale": 1.0,
        "layoutmode": "normal",
        "laparams": LAParams(),
        "codec": "utf-8"
    }
    resource_manager = PDFResourceManager()
    fake_file_handle = io.BytesIO()
    converter = HTMLConverter(resource_manager, fake_file_handle, **params)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        html = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if html:
        return html.decode("utf-8")

print(extract_text_from_pdf("/tmp/wb.pdf"))
