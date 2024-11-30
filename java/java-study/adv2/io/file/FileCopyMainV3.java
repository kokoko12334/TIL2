package adv2.io.file;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

public class FileCopyMainV3 {
    public static void main(String[] args) throws IOException {
        long startTime = System.currentTimeMillis();

        Path soruce = Path.of("temp/copy.dat");
        Path target = Path.of("temp/copy_new.dat");
        // 기존에는 파일 -> 자바 -> 파일 과정이지만 Files는 그냥 바로 운영체제의 레벨에서 바로 복사한다. 즉, 파일 -> 파일로 바로 복사 그래서 제일 빠름.
        Files.copy(soruce, target, StandardCopyOption.REPLACE_EXISTING);

        long endTime = System.currentTimeMillis();
        System.out.println("time taken:" + (endTime - startTime) + "ms");
    }
}
