import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// 숫자 N개 중 소수가 몇 개인지 찾아서 출력

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // 숫자 개수
		int num;
		int count = 0;

		for (int i = 0; i < N; i++) {
			num = sc.nextInt();

			for (int j = 2; j <= num; j++) {
				if (j == num) {
					count += 1;
				}

				// 나누어 떨어지는 숫자가 존재하면 소수가 아님
				if (num % j == 0) {
					break;
				}
			}
		}

		System.out.println(count);
		sc.close();

	}

}
