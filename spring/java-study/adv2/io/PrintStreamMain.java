package adv2.io;

import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

public class PrintStreamMain {
    public static void main(String[] args) throws IOException {

        PrintStream printStream = System.out;

        byte[] bytes = "Hello\n".getBytes(StandardCharsets.UTF_8);
        printStream.write(bytes);


    }
}
