import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Baek1697 {
    static int[] seen = new int[100001];

    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String inputString = reader.readLine();

        String[] split = inputString.split(" ");

        int n = Integer.parseInt(split[0]);
        int k = Integer.parseInt(split[1]);
        System.out.println(bfs(n, k));


    }

    private static int bfs(int n, int k) {
        int result = 0;
        Queue<Integer> queue = new LinkedList<>();
        seen[n] = 0;

        queue.add(n);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            if (current == k) {
                result = seen[current];
                break;

            }

            int a = current - 1;
            int b = current + 1;
            int c = current * 2;

            if (a >= 0 && a < 100001 && seen[a] == 0) {
                queue.add(a);
                seen[a] = seen[current] + 1;
            }
            if (b >= 0 && b < 100001 && seen[b] == 0) {
                queue.add(b);
                seen[b] = seen[current] + 1;
            }
            if (c >= 0 && c < 100001 && seen[c] == 0) {
                queue.add(c);
                seen[c] = seen[current] + 1;
            }

        }
        return result;
    }
}
