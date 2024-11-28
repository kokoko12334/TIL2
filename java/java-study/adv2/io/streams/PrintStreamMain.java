package adv2.io.streams;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;

public class PrintStreamMain {
    public static void main(String[] args) throws IOException {

        FileOutputStream fos = new FileOutputStream("temp/print.txt");
        PrintStream printStream = new PrintStream(fos);
        printStream.println("ddd"); // System.out이랑 같은 기능 사용 가능. 단지 FIleout이므로 파일로 저장됨.
        fos.close();
    }
}
