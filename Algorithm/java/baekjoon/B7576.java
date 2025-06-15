import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B7576 {

	static int[][] MATRIX;
	static int M;
	static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] split = br.readLine().split(" ");

		M = Integer.parseInt(split[0]);
		N = Integer.parseInt(split[1]);

		MATRIX = new int[N][M];
		Queue<int[]> queue = new LinkedList<>();

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int num = Integer.parseInt(st.nextToken());
				MATRIX[i][j] = num;
				if (num == 1) {
					queue.add(new int[] {i, j});
				}
			}
		}

		bfs(queue);

		int answer = resultCheck();
		System.out.println(answer - 1);
	}

	private static void bfs(Queue<int[]> queue) {

		int[] dx = new int[] {1, 0, -1, 0};
		int[] dy = new int[] {0, 1, 0, -1};
		while (!queue.isEmpty()) {
			int[] poll = queue.poll();
			int y = poll[0];
			int x = poll[1];
			int ny;
			int nx;
			for (int i = 0; i < 4; i++) {
				ny = y + dy[i];
				nx = x + dx[i];

				if (nx < 0 || nx >= M || ny < 0 || ny >= N) {
					continue;
				}
				if (MATRIX[ny][nx] > 0 || MATRIX[ny][nx] == -1) {
					continue;
				}

				MATRIX[ny][nx] = MATRIX[y][x] + 1;
				queue.add(new int[] {ny, nx});
			}

		}

	}

	private static int resultCheck() {
		int answer = 0;
		for (int[] arr : MATRIX) {
			for (int num : arr) {
				if (num == 0) {
					return 0;
				}
				if (num == -1) {
					continue;
				}
				answer = Math.max(answer, num);
			}
		}
		return answer;
	}

}
