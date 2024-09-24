"""
폴더를 순회하면서 pdf파일이 나타날 경우 pdf 분리 작업 및 엑셀 생성 작업을 합니다
"""


import os
from natsort import natsorted


from module.create_log import logging
from module.create_excel import create_excel
from module.create_path import _create_path
from module.extract_bookmark import extract_bookmark
from module.extract_name import _extract_cmt, _extract_org
from module.split_pdf import split_pdf_by_bookmarks
from module.data import committee_dict, organization_dict


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

            create_excel(excel_list, excel_path,
                         split_pdf_by_bookmarks(pdf_path, folder_path))
