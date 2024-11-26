package adv2.io.buffer;

import java.io.FileInputStream;
import java.io.IOException;

import static adv2.io.buffer.BufferedConst.FILE_NAME;
import static adv2.io.buffer.BufferedConst.FILE_SIZE;

public class ReadFileV1 {
    public static void main(String[] args) throws IOException {

        FileInputStream fis = new FileInputStream(BufferedConst.FILE_NAME);
        long startTime = System.currentTimeMillis();

        int fileSize = 0;
        int data;
        while ((data = fis.read()) != -1) {
            fileSize++;
        }
        fis.close();
        long endTime = System.currentTimeMillis();
        System.out.println("File create:" + FILE_NAME);
        System.out.println("File size:" + (FILE_SIZE / 1024 / 1024) + "MB");
        System.out.println("Time:" + (endTime - startTime) + "ms");
    }
}
