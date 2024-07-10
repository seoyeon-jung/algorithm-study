import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();

		int money = 0;

		if (A == B && B == C) {
			money = 10000 + A * 1000;
		} else if (A == B || A == C) {
			money = 1000 + A * 100;
		} else if (B == C) {
			money = 1000 + B * 100;
		} else {
			// 모두 다 다를 때
			int max_num = Math.max(A, Math.max(B, C));
			money = max_num * 100;
		}

		System.out.println(money);

		sc.close();
	}
}
