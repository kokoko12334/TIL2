import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Baek1940 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        ArrayList<Integer> list = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i < n; i++){
            list.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(list);

        int l = 0;
        int r = n - 1;
        int answer = 0;
        int num;
        while (l < r){
            num = list.get(l) + list.get(r);
            if (num == m){
                answer += 1;
            }

            if (num <= m){
                l += 1;
            }else {
                r -= 1;
            }
        }

        System.out.println(String.valueOf(answer));
    }
}
