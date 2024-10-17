import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Baek1253 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++){
            list.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(list);
        int l, r, target, num;
        int answer = 0;
        for (int i = 0; i < n; i++){
            l = 0;
            r = n - 1;
            target = list.get(i);
            if (l == i){
                l += 1;
            }else if (r == i) {
                r -= 1;
            }
            while (l < r){
                num = list.get(l) + list.get(r);
                if (num == target){
                    answer += 1;
                    break;
                }

                if (num < target){
                    l += 1;
                }else {
                    r -= 1;
                }
                if (l == i){
                    l += 1;
                }else if (r == i) {
                    r -= 1;
                }
            }

        }
        System.out.println(answer);
    }
}
