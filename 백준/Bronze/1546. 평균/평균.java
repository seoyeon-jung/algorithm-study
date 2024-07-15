import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // 과목의 개수
		int[] n_arr = new int[N]; // 현재 성적 입력
		for (int i = 0; i < n_arr.length; i++) {
			n_arr[i] = sc.nextInt();
		}

		long sum = 0; // 최댓값으로 점수 총합 계산
		long maxScore = 0; // 최댓값 구하기

		for (int i = 0; i < N; i++) {
			if (maxScore < n_arr[i]) {
				maxScore = n_arr[i];
			}
			sum += n_arr[i];
		}
		sc.close();

		System.out.println(sum * 100.0 / maxScore / N);

	}

}
