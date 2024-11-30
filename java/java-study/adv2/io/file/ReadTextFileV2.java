package adv2.io.file;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Stream;

public class ReadTextFileV2 {
    private static final String PATH = "temp/hello2.txt";

    public static void main(String[] args) throws IOException {
        String writeString = "abc\n기ㅏ나다";

        Path path = Path.of(PATH);

        Files.writeString(path, writeString, StandardCharsets.UTF_8);
//
//        // 한꺼번에 가져오기
//        List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);
//        for  (int i = 0; i < lines.size(); i ++) {
//            System.out.println(lines.get(i));
//        }

        // 하나씩 가져와서 읽기
        Stream<String> lineStream = Files.lines(path, StandardCharsets.UTF_8);
        lineStream.forEach(line -> System.out.println(line));
        lineStream.close();
    }
}
