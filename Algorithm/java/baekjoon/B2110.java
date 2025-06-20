import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B2110 {

	static int N;
	static int M;
	static int[] arr;
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}

		Arrays.sort(arr);

		int l = 0;
		int r = 1000000001;
		int m;
		int answer = 0;
		while (l < r) {
			m = (l + r) / 2;

			if (check(m)) {
				l = m + 1;
				answer = Math.max(answer, m);
			} else {
				r = m;
			}

		}

		System.out.println(answer);

	}

	private static boolean check(int m) {

		int cnt = 1;
		int now = arr[0];
		int diff;
		for (int i = 1; i < N; i++) {
			diff = arr[i] - now;
			if (diff < m) {
				continue;
			}

			cnt++;
			now = arr[i];

		}

		return cnt >= M;

	}
}
