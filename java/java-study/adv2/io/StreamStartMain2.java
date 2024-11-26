package adv2.io;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class StreamStartMain2 {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("temp/hello.dat");
        byte[] input = {65, 66, 67};
        fos.write(input);
        fos.close();

        FileInputStream fis = new FileInputStream("temp/hello.dat");
        byte[] buffer = new byte[10];
        int readCount = fis.read(buffer, 1, 4); // off는 배열의 시작점이고 len은 길이(자기자신 포함) 따라서 off =5 이면 배열의 5부터 5,6,7로 3개len까지 채움
        System.out.println(readCount);
        System.out.println(Arrays.toString(buffer));
        fis.close();
    }
}
