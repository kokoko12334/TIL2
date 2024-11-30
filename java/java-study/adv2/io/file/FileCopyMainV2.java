package adv2.io.file;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileCopyMainV2 {
    public static void main(String[] args) throws IOException {
        String fileName = "temp/copy.dat";
        long startTime = System.currentTimeMillis();
        FileInputStream fis = new FileInputStream(fileName);
        FileOutputStream fos = new FileOutputStream("temp/copy_new.dat");
        // 받자마다 바로 넘기기 인풋 스트림 에서 아웃풋스트림으로 바로바로 보내서 속도가 더 빠름.
        fis.transferTo(fos);

        fis.close();
        fos.close();

        long endTime = System.currentTimeMillis();
        System.out.println("FIle Created:" + fileName);
        System.out.println("time taken:" + (endTime - startTime) + "ms");
    }
}
