"""
폴더를 순회하면서 pdf파일이 나타날 경우 pdf 분리 작업을 합니다
"""


import os
from natsort import natsorted


from module.split_pdf import split_pdf_by_bookmarks


def processing_folder(input_folder, output_folder):
    """폴더를 순회하면서 PDF 파일을 처리합니다"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(input_folder):
        for file in natsorted(files):
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join('\\\\?\\', root, file)
                pdf_output_dir = os.path.join('\\\\?\\',
                                              output_folder, os.path.splitext(file)[0])

                split_pdf_by_bookmarks(pdf_path, pdf_output_dir)
