package adv2.io.text;

import java.io.*;
import java.nio.charset.StandardCharsets;

public class ReaderWriterMainV3 {
    public static void main(String[] args) throws IOException {
        String writeString = "absdasd";
        // v2랑 같은거임 내부에서 fileoutputstream 객체를 갔다가 쓴거임.
        FileWriter fw = new FileWriter(TextConst.File_NAME, StandardCharsets.UTF_8);
        fw.write(writeString);
        fw.close();

        StringBuilder str = new StringBuilder();
        FileReader fr = new FileReader(TextConst.File_NAME, StandardCharsets.UTF_8);
        int ch;
        while ((ch = fr.read()) != -1) {
            str.append((char) ch);
        }
        fr.close();
        System.out.println(str);

    }
}
