 #include <stdio.h>

int main()    //main함수는 처음으로 실행되는 함수
{
	printf("Hello, world!\n");
	
	printf("%s\n", "Hello, world2");
	printf("%s, %s\n", "Hello, world2","Hello, world3");
	return 0;       
	
}

// hello.c -> hello.obj -> hello.exe 로 실행 순서

//같은 프로젝트안에서 서로 다른 c파일을 실행하려면 우클릭-> 속성-> 빌드에서 제외 예 누르면 됨.



























