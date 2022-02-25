from uuid import uuid4
from pdf2docx import Converter
import pandas as pd
import numpy as np
from pdf2image import convert_from_path
from pathlib import Path
import shutil
import PyPDF2


def convert_pdf2docx(pdf, id):
    docx = f'media/documents/temp/{id}.docx'
    cv = Converter(pdf)
    cv.convert(docx, multi_processing=True)
    cv.close()
    return docx


def convert_csv2excel(csv, id):
    excel_path = f'media/documents/temp/{id}.xlsx'
    df = pd.read_csv(csv)
    # saving xlsx file
    excel = pd.ExcelWriter(excel_path)
    df.to_excel(excel, index=False)
    excel.save()
    return excel_path


def convert_excel2csv(excel, id):
    csv_path = f'media/documents/temp/{id}.csv'
    read_file = pd.read_excel(excel)
    read_file.to_csv(csv_path, index=None, header=True)
    return csv_path


def convert_pdf2image(pdf, uid):
    temp_dir = Path('media/documents/temp')
    image = temp_dir / f'{uid}'
    zip_path = temp_dir / f'{uid}.zip'

    image.mkdir(parents=True, exist_ok=True)

    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf)

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'{image}/page{str(i)}.jpg', 'JPEG')

    shutil.make_archive(image, 'zip', image)
    shutil.rmtree(image)
    return zip_path


def pdf_merge(pdf1, pdf2, id):
    pdf_path = f'media/documents/temp/{id}.pdf'
    mergeFile = PyPDF2.PdfFileMerger()

    mergeFile.append(PyPDF2.PdfFileReader(pdf1, 'rb'))

    mergeFile.append(PyPDF2.PdfFileReader(pdf2, 'rb'))

    mergeFile.write(pdf_path)

    return pdf_path
