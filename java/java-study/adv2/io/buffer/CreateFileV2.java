package adv2.io.buffer;

import java.io.FileOutputStream;
import java.io.IOException;

import static adv2.io.buffer.BufferedConst.*;

public class CreateFileV2 {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream(FILE_NAME);
        long startTime = System.currentTimeMillis();

        byte[] buffer = new byte[BUFFER_SIZE];
        int bufferIndex = 0;

        for (int i = 0; i < FILE_SIZE; i++) {
            buffer[bufferIndex] = 1;
            bufferIndex++;
            if (bufferIndex == BUFFER_SIZE) {
                fos.write(buffer);
                bufferIndex = 0;
            }
        }
        System.out.println(bufferIndex);
        if (bufferIndex > 0) {
            fos.write(buffer, 0, bufferIndex);
        }

        fos.close();
        long endTime = System.currentTimeMillis();
        System.out.println("File create:" + FILE_NAME);
        System.out.println("File size:" + (FILE_SIZE / 1024 / 1024) + "MB");
        System.out.println("Time:" + (endTime - startTime) + "ms");

    }
}
