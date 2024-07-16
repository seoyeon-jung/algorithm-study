import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // 배열 길이
		int M = sc.nextInt(); // 반복 횟수

		int[] arr = new int[N]; // 바구니 배열

		for (int i = 0; i < M; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			int z = sc.nextInt();

			for (int j = x - 1; j < y; j++) {
				// 입력받은 줄에서 반복
				arr[j] = z;
			}
		}

		for (int i = 0; i < N; i++) {
			System.out.print(arr[i] + " ");
		}

		sc.close();
	}
}
