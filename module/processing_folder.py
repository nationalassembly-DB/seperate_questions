"""
폴더를 순회하면서 pdf파일이 나타날 경우 pdf 분리 작업 및 엑셀 생성 작업을 합니다
"""


import os
import sys
from pathlib import Path
from natsort import natsorted


from module.create_log import logging
from module.create_excel import create_excel
from module.create_path import _create_path
from module.extract_bookmark import extract_bookmark
from module.extract_name import _extract_cmt, _extract_org
from module.split_file import split_pdf_folder
from module.split_pdf import split_pdf_by_bookmarks
from module.data import committee_dict, organization_dict


def processing_script():
    """북마크를 사용하여 주질의마다 PDF를 분할합니다"""
    print("[1] PDF분할 (파일 500개 이상 자동처리)")
    print("[2] 파일 500개 이상 분할하기")
    print("[0] 스크립트 종료")
    input_num = input("=> ")

    match input_num:
        case '1':
            input_path = input("작업할 폴더 경로를 입력해주세요.\n=> ")
            output_path = input("분할된 PDF와 엑셀 파일을 저장할 경로를 입력해주세요.\n=> ")
            processing_folder(input_path, output_path)
        case '2':
            root_folder_path = input("PDF 파일이 들어 있는 루트 폴더 경로를 입력하세요.\n=> ")
            processing_split_files(root_folder_path)
        case '0':
            sys.exit()
        case _:
            print("\n=====올바른 숫자를 입력해주세요=====\n")


def processing_folder(input_path, output_path):
    """폴더를 순회하면서 PDF 파일을 처리합니다"""
    for root, _, files in os.walk(input_path):
        for file in natsorted(files):
            excel_list = []

            if not file.lower().endswith('.pdf'):
                continue
            pdf_path = os.path.join('\\\\?\\', root, file)

            cmt = _extract_cmt(file)
            org = _extract_org(file)
            up_name = (str(committee_dict[cmt]) if cmt in committee_dict else "test_cmt") + '_' + \
                (organization_dict[org]
                 if org in organization_dict else "test_org")

            for item in extract_bookmark(pdf_path):
                try:
                    if len(item) <= 1 or item['level'] != 3:
                        continue

                    excel_list.append({
                        "cmt": cmt,
                        "org": org,
                        "name": item['parent']['title'],
                        "question": item['title'],
                        "realfile_name": file
                    })
                except Exception as e:  # pylint: disable=W0703
                    e = "PDF 북마크 추출 오류"
                    logging(e, '', input_path)

            folder_path, excel_path = _create_path(
                output_path, up_name)

            if (create_excel(excel_list, excel_path, split_pdf_by_bookmarks(
                    pdf_path, folder_path, file), output_path) < 500):
                continue
            split_pdf_folder(folder_path)


def processing_split_files(root_folder_path):
    """주어진 폴더와 그 하위 폴더들에 대해 PDF 분할 작업을 수행"""
    root_folder_path = Path(root_folder_path)
    for subfolder in root_folder_path.rglob('*'):
        if subfolder.is_dir():
            split_pdf_folder(subfolder)
