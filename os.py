import encodings
import os


#경로 확인
os.getcwd()

#경로 수정

os.chdir("C:/Users/user/Desktop/file")


#파일 목록 확인(터미널에서 실행)
os.system('dir')

#결과값 받아오기
r = os.popen('dir').read()
print(r)



