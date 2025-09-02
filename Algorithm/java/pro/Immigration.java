
public class Immigration {

	public long solution(int n, int[] times) {
		long answer = Long.MAX_VALUE;
		long left = 0;
		long right = 1000000000000000001L;
		long mid;
		while (left < right) {
			mid = (left + right) / 2;

			if (check(mid,times, n)) {
				right = mid;
				answer = Math.min(answer, mid);
			} else {
				left = mid + 1;
			}
		}

		return answer;
	}

	private boolean check(long mid, int[] times, int n) {
		long cnt = 0;

		for (int time: times) {
			cnt += (long)Math.floor(mid/time);
		}
		System.out.println("mid: " + mid + " " + "cnt: " + cnt);

		return cnt >= n;
	}
}
