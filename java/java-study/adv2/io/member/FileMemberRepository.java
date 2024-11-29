package adv2.io.member;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FileMemberRepository implements MemberRepository{

    private static final String FILE_PATH = "temp/members-txt.dat";
    private static final String DELIMITER = ",";

    @Override
    public void add(Member member) {

        try(BufferedWriter bw = new BufferedWriter(new FileWriter(FILE_PATH, true))) {
            bw.write(member.getId() + DELIMITER + member.getName() + DELIMITER + member.getAge());
            bw.newLine();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

    @Override
    public List<Member> finAll() {
        List<Member> members = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(FILE_PATH))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] memberData = line.split(DELIMITER);
                Member member = new Member(memberData[0], memberData[1], Integer.valueOf(memberData[2]));
                members.add(member);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return members;
    }
}
