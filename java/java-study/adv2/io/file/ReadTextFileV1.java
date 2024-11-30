package adv2.io.file;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class ReadTextFileV1 {
    private static final String PATH = "temp/hello2.txt";

    public static void main(String[] args) throws IOException {
        String writeString = "abc\n기ㅏ나다";

        Path path = Path.of(PATH);

        Files.writeString(path, writeString, StandardCharsets.UTF_8);
        String readString = Files.readString(path, StandardCharsets.UTF_8);
        System.out.println(readString);
    }
}
