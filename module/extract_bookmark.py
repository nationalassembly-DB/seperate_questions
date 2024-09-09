"""
북마크를 추출하고 level, title, page, parent북마크 리스트로 반환합니다.
"""

import fitz


def _parse_toc(toc):
    """추출한 북마크의 정보들을 취합하여 리스트로 저장합니다"""
    bookmarks = []

    for item in toc:
        level, title, page, _ = item
        bookmarks.append({
            "level": level,
            "title": title,
            "page": page - 1,
            "parent": None
        })

    for i in range(1, len(bookmarks)):
        for j in range(i-1, -1, -1):
            if bookmarks[j]['level'] < bookmarks[i]['level']:
                bookmarks[i]['parent'] = bookmarks[j]
                break

    return bookmarks


def extract_bookmark(pdf_path):
    """pdf에서 북마크를 추출합니다"""
    doc = fitz.open(pdf_path)
    toc = doc.get_toc(simple=False)
    return _parse_toc(toc)
