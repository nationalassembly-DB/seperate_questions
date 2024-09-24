"""
extact_name.py

위원회와 피감기관을 파일명에서 추출합니다
"""

import re


def _extract_cmt(filename):
    # 파일명에서 위원회 이름 추출
    first_underscore_index = filename.find('_')
    second_underscore_index = filename.find(
        '_', first_underscore_index + 1)
    if first_underscore_index != -1 and second_underscore_index != -1:
        cmt = filename[first_underscore_index +
                       1:second_underscore_index]
    else:
        cmt = ""

    return cmt


def _extract_org(filename):
    # 파일명에서 피감기관 이름 추출
    org_matches = re.findall(r'\(([^)]+)\)', filename)
    if org_matches:
        org = org_matches[-1]
        if org == '2':
            org = org_matches[-2]
        if str(org).endswith('(주'):
            org = str(org).replace('(주', '(주)')
    else:
        org = ""

    return org
