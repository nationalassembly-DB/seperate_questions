"""
create_path.py

folder path나 file path 등을 입력받은 데이터로 토대로 경로명을 반환합니다.
"""

import os


def _create_path(output_path, pre_folder_path):
    """위원회, 기관 코드로 이루어진 upload_name을 입력받아 권 수가 포함된 폴더 경로로 반환"""
    i = 1

    while True:
        book_num = str(i).zfill(2)
        folder_path = os.path.join(
            '\\\\?\\', output_path, pre_folder_path + '_' + book_num)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            break
        i += 1

    excel_path = os.path.join(
        '\\\\?\\', folder_path, f"{os.path.basename(folder_path)}.xlsx")

    return folder_path, excel_path
