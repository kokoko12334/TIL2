package adv2.io.streams;

import java.io.*;

public class DataStreamMain {
    public static void main(String[] args) throws IOException {
        // datastream은 자바의 데이터형을 그대로 반영
        FileOutputStream fos = new FileOutputStream("temp/data.dat");
        DataOutputStream dos = new DataOutputStream(fos);

        dos.writeUTF("회원A");
        dos.writeInt(20);
        dos.writeBoolean(true);
        dos.close();
        
        FileInputStream fis = new FileInputStream("temp/data.dat");
        DataInputStream dis = new DataInputStream(fis);
        System.out.println(dis.readUTF());
        System.out.println(dis.readInt());
        System.out.println(dis.readBoolean()); // 저장한 순서대로 무조건 데이터타입을 맞추어 read 해야함.
        dis.close();
    }
}
