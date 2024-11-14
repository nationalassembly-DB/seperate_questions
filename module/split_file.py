"""폴더를 원하는 갯수만큼 폴더에 나눠서 이동합니다"""


from pathlib import Path
import shutil


def split_pdf_folder(input_folder_path):  # pylint: disable = R0914
    """폴더를 원하는 갯수만큼 폴더에 나눠서 이동합니다"""
    input_folder_path = Path(input_folder_path)
    if not input_folder_path.is_dir():
        print(f"지정한 폴더 경로가 존재하지 않습니다: {input_folder_path}")
        return

    all_files = list(input_folder_path.iterdir())
    pdf_files = [f for f in all_files if f.is_file()
                 and f.suffix.lower() == '.pdf']
    excel_files = [f for f in all_files if f.is_file() and f.suffix.lower() in [
        '.xlsx', '.xls']]

    if len(pdf_files) < 500:
        return

    base_folder_name = input_folder_path.name

    first_folder_name = f"{base_folder_name}_01"
    first_folder_path = input_folder_path / first_folder_name

    if not first_folder_path.exists():
        first_folder_path.mkdir()

    for excel_file in excel_files:
        dest_path = first_folder_path / excel_file.name
        shutil.move(str(excel_file), str(dest_path))

    first_folder_pdf_files = pdf_files[:300 - len(excel_files)]
    for pdf_file in first_folder_pdf_files:
        dest_path = first_folder_path / pdf_file.name
        shutil.move(str(pdf_file), str(dest_path))

    remaining_pdf_files = pdf_files[300 - len(excel_files):]
    folder_count = 1

    for i in range(0, len(remaining_pdf_files), 300):
        folder_count += 1
        new_folder_name = f"{base_folder_name}_{folder_count:02d}"
        new_folder_path = input_folder_path / new_folder_name

        if not new_folder_path.exists():
            new_folder_path.mkdir()

        folder_pdf_files = remaining_pdf_files[i:i + 300]

        for pdf_file in folder_pdf_files:
            dest_path = new_folder_path / pdf_file.name
            shutil.move(str(pdf_file), str(dest_path))

    print("PDF 파일이 성공적으로 나눠졌습니다.")
