import os
import fitz


from module.extract_bookmark import extract_bookmark


def _init_filename(title, output_dir):
    """파일명에 적합하지 않은 문자를 제거하고 안전한 파일명을 반환합니다"""
    return os.path.join('\\\\?\\', output_dir,
                        f"{title.replace('/', '_').replace('\\', '_')
                           .replace(':', '_').replace('*', '_').replace('?', '_')
                           .replace('"', '_').replace('<', '_').replace('>', '_')
                           .replace('|', '_')}.PDF")


def split_pdf_by_bookmarks(pdf_path, output_dir):
    """북마크에 따라 PDF를 분할하고 저장합니다"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = fitz.open(pdf_path)
    bookmarks = extract_bookmark(pdf_path)
    filename_tmp = 1

    for bookmark in bookmarks:
        if bookmark['level'] == 3:
            start_page = bookmark['page']
            next_bookmark = next(
                (b for b in bookmarks if b['level'] == 3 and b['page'] > start_page), None)
            end_page = next_bookmark['page'] - \
                1 if next_bookmark else doc.page_count - 1

            if start_page > end_page:
                continue

            new_pdf = fitz.open()
            for p in range(start_page, end_page + 1):
                new_pdf.insert_pdf(doc, from_page=p, to_page=p)

            new_toc_list = [[1, bookmark['title'], 0]]
            new_pdf.set_toc(new_toc_list)

            # 파일명을 북마크로 저장할경우 아래 주석 해제
            # output_path = _init_filename(
            #     bookmark['title'], output_dir)
            output_path = os.path.join(
                '\\\\?\\', output_dir, f"{filename_tmp}.PDF")
            new_pdf.save(output_path)
            new_pdf.close()
            filename_tmp += 1

    doc.close()
