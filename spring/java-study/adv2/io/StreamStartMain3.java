package adv2.io;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class StreamStartMain3 {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("temp/hello.dat");
        byte[] arr = fis.readAllBytes();
        System.out.println(Arrays.toString(arr));
        fis.close();

    }
}
