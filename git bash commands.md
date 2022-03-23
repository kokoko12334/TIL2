# 1.git bash 명령어

- ### 생성/삭제

  - `mkdir <name>`: 폴더 생성
  - `touch <name.확장자>`: 해당 확장자 파일 생성
  - `vi <name.확장자>`:  파일 생성 및 편집
    - `i`: insert 시작, 내용삽입 다 끝나면 esc
    - `:q`: 그냥 종료
    - `:wq`: 저장하고 종료

  - `rm <name>`:파일 삭제

  - `rm -r <name>`:폴더 삭제

  - `rm -i <name>`: 삭제 할것인지를 확인

  - `rm -i <name>*`:모든 파일 삭제

    

- ### 경로 이동

  - `cd ..`:상위 폴더로 이동

  - `cd <path>`: 해당 경로로 이동

  - `cd <path1>/<path2>`: path2로 한번에 이동

  - `cd ../..`: 두칸의 상위 폴더로 이동

    

- ### 기타

  - `ls`: 해당 폴더 내용 확인
  - `ls -a`: 숨김폴더 까지 확인
  - `start .`: 해당 폴더 열기
  - `start <name>`: 해당 파일 열기
  - `mv <file> <folder>`: 파일을 폴더로 이동
  - `mv <file> <file2>`: 파일명을 fil2로 수정
  - `clear`: 배쉬안의 내용 삭제
  - `code .`:visual studio code 실행
  - `pwd`: 내 위치 조회
  - `cat > <name>`: 파일, 내용 생성
  - `cat <name>`: 파일 내용 조회(`more <name>`는  조금 씩)
  - `./<name>`: 파일 실행
  - `ps -ef | grep jupy | grep lab03`: putty에서 연결 되었는지 확인(lab03은 유저이름)

> edujihye21@gmail.com(강사님 이메일)