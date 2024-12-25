import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Baek1005 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int test = Integer.parseInt(br.readLine());

        for (int i=0; i<test; i++) {
            String[] strings = br.readLine().split(" ");
            int n = Integer.parseInt(strings[0]);
            int k = Integer.parseInt(strings[1]);
            List<Integer> arr = Arrays.stream(br.readLine().split(" "))
                        .map(Integer::parseInt)
                        .toList();
            Map<Integer, List<Integer>> graph = new HashMap<>();

            List<Integer> countArr = new ArrayList<>(Collections.nCopies(n, 0));

            for (int j=0; j<k; j++) {
                String[] strings2 = br.readLine().split(" ");
                int a = Integer.parseInt(strings[0]) - 1;
                int b = Integer.parseInt(strings[1]) - 1;
                List<Integer> temp = graph.get(a);
                temp.add(b);
                graph.put(a, temp);
                countArr.set(b, countArr.get(b) + 1);
            }

            int target = Integer.parseInt(br.readLine()) - 1;
            Deque<List<Integer>> queue = new ArrayDeque<>();
            List<Integer> visited = new ArrayList<>(Collections.nCopies(n, 0));
            for (int o=0; o <n; o++) {
                if (countArr.get(o) == 0) {
                    queue.add(new ArrayList<>(Arrays.asList(o, arr.get(o))));
                    visited.set(o, arr.get(o));
                }
            }
            int result = bfs(queue, visited);
            System.out.println(result);

        }


    }

    private static int bfs(Deque<List<Integer>> queue, List<Integer> visited) {
        
        return 0;
    }
}
