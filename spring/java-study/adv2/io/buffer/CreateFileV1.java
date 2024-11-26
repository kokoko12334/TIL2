package adv2.io.buffer;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import static adv2.io.buffer.BufferedConst.*;

public class CreateFileV1 {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream(FILE_NAME);
        long startTime = System.currentTimeMillis();

        for (int i = 0; i < FILE_SIZE; i++) {
            fos.write(1);
        }
        fos.close();
        long endTime = System.currentTimeMillis();
        System.out.println("File create:" + FILE_NAME);
        System.out.println("File size:" + (FILE_SIZE / 1024 / 1024) + "MB");
        System.out.println("Time:" + (endTime - startTime) + "ms");

    }
}
