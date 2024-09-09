"""
북마크에서 주질의를 찾아내 각 pdf 파일로 split 합니다. 
"""


import os


from module.processing_folder import processing_folder


def main():
    """북마크를 사용하여 주질의마다 PDF를 분할합니다"""
    print("\n>>>>>>주질의 PDF 분할<<<<<<\n")
    print("-"*24)
    input_path = input("작업할 폴더 경로를 입력하세요(종료는 0을 입력) : ").strip()

    if input_path == '0':
        return 0

    output_path = input(
        "split된 PDF가 저장될폴더 경로를 입력하세요 : ").strip()

    if not os.path.isdir(input_path) and not os.path.isdir(output_path):
        print("폴더 경로를 다시 확인하세요")
        return main()

    processing_folder(input_path, output_path)
    print("-"*24)
    print(f"{output_path}에 분할된 PDF가 저장되었습니다.")
    print("\n~~~모든 작업이 완료되었습니다~~~")

    return main()


if __name__ == "__main__":
    main()
