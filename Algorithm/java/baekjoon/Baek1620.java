import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Baek1620 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ints = br.readLine().split(" ");
        int n = Integer.parseInt(ints[0]);
        int m = Integer.parseInt(ints[1]);

        Map<String, Integer> map = new HashMap<>();
        String[] arr = new String[n+1];

        String name;
        for (int i = 0; i < n; i++){
            name = br.readLine();
            map.put(name, i+1);
            arr[i+1] = name;
        }

        String p;
        int num;
        for (int i = 0; i < m; i++){
            p = br.readLine();
            try {
                num = Integer.parseInt(p);
                System.out.println(arr[num]);
            } catch (NumberFormatException e){
                System.out.println(map.get(p));
            }
        }

    }
}
