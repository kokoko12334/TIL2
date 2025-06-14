import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class B1931 {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int[][] rooms = new int[n][2];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 2; j++) {
				int time = Integer.parseInt(st.nextToken());
				rooms[i][j] = time;
			}
		}

		// Arrays.sort(rooms, Comparator.comparingInt((int[] i) -> i[0]).thenComparingInt((int[] i) -> i[1]).reversed());
		// Arrays.sort(rooms, Comparator.comparingInt((int[] i) -> i[0]));
		Arrays.sort(rooms, Comparator.comparingInt((int[] i) -> i[1])
			.thenComparingInt((int[] i) -> i[0])
		);
		// for (int[] arr : rooms) {
		// 	System.out.println(Arrays.toString(arr));
		// }

		int end = 0;
		int answer = 0;
		for (int i = 0; i < n; i++) {
			if (end <= rooms[i][0]) {
				end = rooms[i][1];
				answer += 1;
			}
		}
		System.out.println(answer);
	}
}