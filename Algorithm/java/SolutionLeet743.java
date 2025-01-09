import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class SolutionLeet743 {

    public int networkDelayTime(int[][] times, int n, int k) {

        final int INF = Integer.MAX_VALUE / 2;

        int[][] matrix = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(matrix[i], INF);
            matrix[i][i] = 0;
        }

        for (int[] time : times) {
            int u = time[0], v = time[1], w = time[2];
            matrix[u][v] = w;
        }

        int[] result = dij(k, matrix, n, INF);

        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (result[i] == INF) {
                return -1;
            }
            answer = Math.max(answer, result[i]);
        }
        return answer;
    }

    private int[] dij(int start, int[][] matrix, int n, int INF) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[] dis = Arrays.copyOf(matrix[start], n + 1);

        for (int i = 1; i <= n; i++) {
            if (i != start && matrix[start][i] != INF) {
                pq.offer(new int[]{matrix[start][i], i});
            }
        }

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int cost = current[0], node = current[1];

            for (int i = 1; i <= n; i++) {
                if (matrix[node][i] != INF && matrix[node][i] + cost < dis[i]) {
                    dis[i] = matrix[node][i] + cost;
                    pq.offer(new int[]{dis[i], i});
                }
            }
        }

        return dis;
    }

}
