package adv2.io.buffer;

import java.io.BufferedOutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import static adv2.io.buffer.BufferedConst.*;

public class CreateFileV3 {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream(FILE_NAME);
        BufferedOutputStream bos = new BufferedOutputStream(fos, BUFFER_SIZE);
        long startTime = System.currentTimeMillis();

        for (int i = 0; i < FILE_SIZE; i++) {
            bos.write(1); // 버퍼에 쓰다가 버퍼사이즈 다 쓰면 그떄 flush
        }
        bos.close(); // 남은 부분을 flush를 함. 즉, close하기전에 한번 flush를 한다.

        long endTime = System.currentTimeMillis();
        System.out.println("File create:" + FILE_NAME);
        System.out.println("File size:" + (FILE_SIZE / 1024 / 1024) + "MB");
        System.out.println("Time:" + (endTime - startTime) + "ms");

    }
}
