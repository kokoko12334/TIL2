package adv2.io.text;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class ReaderWriterMainV2 {
    public static void main(String[] args) throws IOException {
        String writeString = "ABC";
        // 문자열 취급 관련 클래스는 Writer, Reader 클래스이고 이들을 상속한거임.
        // 스트림 즉 컴퓨터는 바이트 배열만 취급 이떄 일일이 문자열을 바이트로 바꾸고 하는게 불편해서 알아서 해주는 것이 이거임.
        //파일에 쓰기
        FileOutputStream fos = new FileOutputStream(TextConst.File_NAME); // 바이트처리
        OutputStreamWriter osw = new OutputStreamWriter(fos, StandardCharsets.UTF_8); // 문자 자동 처리
        osw.write(writeString);
        osw.close();

        // 파일에서 읽기
        FileInputStream fis = new FileInputStream(TextConst.File_NAME);
        InputStreamReader isr = new InputStreamReader(fis, StandardCharsets.UTF_8);

        StringBuilder sb = new StringBuilder();
        int ch;
        while ((ch = isr.read()) != -1) {
            sb.append((char)ch);
        }
        isr.close();
        System.out.println(sb);
    }
}
