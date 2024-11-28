import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Baek1107 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼(문자열처리리더(바이트처리 리더))

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        List<Character> no = new ArrayList<>();
        if (m > 0) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                String token = st.nextToken();
                char ch = token.charAt(0);
                no.add(ch);
            }
        }
        int minn = Math.abs(n - 100);
        String stringNum;
        boolean flag;
        for (int i = 0; i <= 1000001; i++){
            stringNum = Integer.toString(i);
            flag = true;
            for (int j = 0; j < stringNum.length(); j++){
                if(no.contains(stringNum.charAt(j))){
                    flag = false;
                    break;
                }
            }
            if (flag){
                minn = Math.min(minn, stringNum.length() + Math.abs(n - i));
            }
        }

        System.out.print(String.valueOf(minn));

    }
}
