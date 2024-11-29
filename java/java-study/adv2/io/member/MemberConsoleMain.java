package adv2.io.member;

import java.util.List;
import java.util.Scanner;

public class MemberConsoleMain {
    private static final MemberRepository repository = new ObjectMemberRepository();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("1.회원등록 | 2. 회원 목록 조회 | 3. 종료");
            System.out.println("선택: ");
            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    registerMember(sc);
                    break;
                case 2:
                    displayMembers();
                    break;
                case 3:

                    return;
                default:
                    System.out.println("잘못 입력");
            }
        }
    }

    private static void registerMember(Scanner sc) {
        System.out.println("아이디 입력:");
        String id = sc.nextLine();

        System.out.println("Name입력: ");
        String name = sc.nextLine();

        System.out.println("age 입력: ");
        int age = sc.nextInt();
        sc.nextLine();

        Member newMember = new Member(id, name, age);
        repository.add(newMember);
        System.out.println("등록 성공");
    }

    private static void displayMembers() {
        List <Member> members = repository.finAll();
        System.out.println("회원목록:");
        for (Member member: members) {
           System.out.println(member.toString());
        }
    }
}
