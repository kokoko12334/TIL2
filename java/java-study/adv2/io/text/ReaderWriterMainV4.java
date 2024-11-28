package adv2.io.text;

import java.io.*;
import java.nio.charset.StandardCharsets;

public class ReaderWriterMainV4 {
    private static final int BUFFER_SIZE = 8192;

    public static void main(String[] args) throws IOException {
        String writeString = "가나다다다다다\ndsdsdsds";
        // v2랑 같은거임 내부에서 fileoutputstream 객체를 갔다가 쓴거임.
        FileWriter fw = new FileWriter(TextConst.File_NAME, StandardCharsets.UTF_8);
        BufferedWriter bw = new BufferedWriter(fw, BUFFER_SIZE);
        bw.write(writeString);
        bw.close();

        StringBuilder str = new StringBuilder();
        FileReader fr = new FileReader(TextConst.File_NAME, StandardCharsets.UTF_8);
        BufferedReader br = new BufferedReader(fr, BUFFER_SIZE);

        String line;
        while ((line = br.readLine()) != null) {
            str.append(line).append("\n");
        }
        br.close();
        System.out.println(str);

    }
}
