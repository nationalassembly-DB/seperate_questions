"""
seperate_questions.py

main()
북마크에서 주질의를 찾아내 각 pdf 파일로 split 합니다. 
"""


import os


from module.processing_folder import processing_folder


def main():
    """북마크를 사용하여 주질의마다 PDF를 분할합니다"""
    print("-"*30)
    print("\n>>>>>>주질의 PDF 분할 및 의정자료 업로드 파일 생성<<<<<<\n")
    print("-"*30)
    input_path = input("작업할 폴더 경로를 입력하세요(종료는 0을 입력) : ").strip()

    if input_path == '0':
        return 0

    output_path = input(
        "split된 PDF, 엑셀을 저장할 폴더 경로를 입력하세요 : ").strip()

    if not os.path.isdir(input_path) and not os.path.isdir(output_path):
        print("폴더 경로를 다시 확인하세요")
        return main()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    print("-"*24)
    print("\n작업중입니다. 데이터가 손상될 수 있으니 데이터를 수정하지 마세요.\n")
    processing_folder(input_path, output_path)
    print("-"*24)
    print(f"{output_path}에 분할된 PDF가 저장되었습니다.")
    print("\n~~~모든 작업이 완료되었습니다~~~\n")

    return main()


if __name__ == "__main__":
    main()
