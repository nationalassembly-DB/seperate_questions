"""
extact_name.py

위원회와 피감기관을 파일명에서 추출합니다
"""


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
    # 파일명에서 가장 바깥 괄호를 기준으로 기관 이름 추출
    stack = []
    start = None
    org = ""

    for i, char in enumerate(filename):
        if char == '(':
            stack.append(i)
            if len(stack) == 1:
                start = i
        elif char == ')':
            stack.pop()
            if len(stack) == 0:
                org = filename[start + 1:i]
                break

    if not org:
        org = ""

    return org
