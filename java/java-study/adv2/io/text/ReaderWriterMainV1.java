package adv2.io.text;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class ReaderWriterMainV1 {
    public static void main(String[] args) throws IOException {
        String writeString = "ABC";

        byte[] writeBytes = writeString.getBytes(StandardCharsets.UTF_8);
        System.out.println(writeString);
        System.out.println(Arrays.toString(writeBytes));

        //파일에 쓰기
        FileOutputStream fos = new FileOutputStream(TextConst.File_NAME);
        fos.write(writeBytes);
        fos.close();

        // 파일에서 읽기
        FileInputStream fis = new FileInputStream(TextConst.File_NAME);
        byte[] readBytes = fis.readAllBytes();
        fis.close();

        String str = new String(readBytes, StandardCharsets.UTF_8);
        System.out.println(str);
    }
}
