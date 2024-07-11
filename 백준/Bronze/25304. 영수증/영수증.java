import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 구매한 각 물건의 가격과 개수
		// 물건들 총액
		// 영수증 금액과 일치하는지 검사 -> 일치하면 Yes, 아니면 No

		int X = sc.nextInt(); // 영수증에 적힌 총 금액
		int N = sc.nextInt(); // 구매한 물건의 종류

		int sum = 0; // 물건들 총액

		for (int i = 1; i <= N; i++) {
			int a = sc.nextInt(); // 물건의 가격
			int b = sc.nextInt(); // 물건의 개수
			int price = a * b;
			sum += price;
		}

		if (sum == X) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}

		sc.close();
	}

}
