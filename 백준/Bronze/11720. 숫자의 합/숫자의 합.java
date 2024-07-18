import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); // 숫자의 개수
		String num = sc.next(); // 공백없이 숫자 N개
		sc.close();

		int sum = 0;

		for (int i = 0; i < N; i++) {
			sum += num.charAt(i) - '0';
		}

		System.out.println(sum);

	}

}
