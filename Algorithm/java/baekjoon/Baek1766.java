import java.io.*;
import java.util.*;

public class Baek1766 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] entry = new int[n+1];

        Map<Integer, List<Integer>> graph = new HashMap<>();

        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            entry[node2]++;
            graph.putIfAbsent(node1, new ArrayList<>());
            graph.get(node1).add(node2);
        }

        PriorityQueue<Integer> hq = new PriorityQueue<>();
        for (int i = 1; i <= n; i++){
            if (entry[i] == 0){
                hq.offer(i);
            }
        }

        List<Integer> answer = new ArrayList<>();

        while (!hq.isEmpty()){
            int num = hq.poll();
            answer.add(num);

            List<Integer> nextNodes = graph.get(num);
            if (nextNodes != null){
                for (int next: nextNodes){
                    entry[next]--;
                    if(entry[next] == 0){
                        hq.offer(next);
                    }
                }
            }
        }

        for (int num : answer){
            System.out.print(num + " ");
        }

    }

}
