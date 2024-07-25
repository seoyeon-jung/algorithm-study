import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		// 테스트 케이스 T
		int t = sc.nextInt();

		for (int i = 0; i < t; i++) {
			// 거스름돈 C (단위는 센트)
			int c = sc.nextInt();

			// 쿼더 = 0.25 / 다임 = 0.10 / 니켈 = 0.05 / 페니 = 0.01
			int quarter = c / 25;
			c = c % 25;

			int dime = c / 10;
			c = c % 10;

			int nickel = c / 5;
			c = c % 5;

			int penny = c;

			System.out.println(quarter + " " + dime + " " + nickel + " " + penny);
		}

		sc.close();

	}

}
