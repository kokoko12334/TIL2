package adv2.io.file;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileCopyMainV1 {
    public static void main(String[] args) throws IOException {
        String fileName = "temp/copy.dat";
        long startTime = System.currentTimeMillis();
        FileInputStream fis = new FileInputStream(fileName);
        FileOutputStream fos = new FileOutputStream("temp/copy_new.dat");

        byte[] bytes = fis.readAllBytes();
        fos.write(bytes);
        fis.close();
        fos.close();

        long endTime = System.currentTimeMillis();
        System.out.println("FIle Created:" + fileName);
        System.out.println("time taken:" + (endTime - startTime) + "ms");
    }
}
