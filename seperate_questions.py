"""
seperate_questions.py

main()
북마크에서 주질의를 찾아내 각 pdf 파일로 split 합니다. 
"""


from module.processing_folder import processing_script


def main():
    """Main 함수"""
    print("-"*30)
    print("\n>>>>>>주질의 PDF 분할 및 의정자료 업로드 파일 생성<<<<<<\n")
    print("-"*30)

    processing_script()

    return main()


if __name__ == "__main__":
    main()
