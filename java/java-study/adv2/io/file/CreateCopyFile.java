package adv2.io.file;

import java.io.FileOutputStream;
import java.io.IOException;

public class CreateCopyFile {

    private static final int FILE_SIZE = 200 * 1024 * 1024;

    public static void main(String[] args) throws IOException {
        String fileName = "temp/copy.dat";
        long startTime = System.currentTimeMillis();
        FileOutputStream fos = new FileOutputStream(fileName);
        byte[] buffer = new byte[FILE_SIZE];
        fos.write(buffer);
        fos.close();
        long endTime = System.currentTimeMillis();
        System.out.println("FIle Created:" + fileName);
        System.out.println("file size:" + FILE_SIZE / 1024 / 1024 + "MB");
        System.out.println("time taken:" + (endTime - startTime) + "ms");
    }
}
