import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Baek16940 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        Map<Integer, Set<Integer>> graph = new HashMap<>();

        for(int i=0; i<n-1; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.putIfAbsent(a, new HashSet<>());
            graph.putIfAbsent(b, new HashSet<>());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        st = new StringTokenizer(br.readLine(), " ");
        List<Integer> path = new ArrayList<>();
        for (int i=0; i<n; i++) {
            path.add(Integer.parseInt(st.nextToken()));
        }

        int answer = 1;

        if (path.get(0) != 1) {
            answer = 0;
        } else {
            Set<Integer> seen = new HashSet<>();
            seen.add(1);
            Deque<Set<Integer>> order = new ArrayDeque<>();
            Set<Integer> next_node = graph.get(1);
            for (int i=1; i < n; i++) {
                if (next_node.isEmpty()) {
                    next_node = order.removeFirst();
                }
                int num = path.get(i);
                if (next_node.contains(num)) {
                    next_node.remove(num);
                    seen.add(num);

                    Set<Integer> add_node = new HashSet<>(graph.get(num));
                    add_node.removeAll(seen);
                    if (!add_node.isEmpty()) {
                        order.add(add_node);
                    }
                }else {
                 answer = 0;
                 break;
                }
            }
        }
        System.out.println(answer);
    }
}
