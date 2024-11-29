package adv2.io.member;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class DataMemberRepository implements MemberRepository{
    private static final String FILE_PATH = "temp/members-data-txt.dat";
    // gnjgnj koko 100000000
    @Override
    public void add(Member member) {
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(FILE_PATH, true))) {
            dos.writeUTF(member.getId());
            dos.writeUTF(member.getName());
            dos.writeInt(member.getAge());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

    @Override
    public List<Member> finAll() {
        List<Member> members = new ArrayList<>();
        try (DataInputStream dis = new DataInputStream(new FileInputStream(FILE_PATH))) {
            while (dis.available() > 0) {
                Member member = new Member(dis.readUTF(), dis.readUTF(), dis.readInt());
                members.add(member);
            }
            return members;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
