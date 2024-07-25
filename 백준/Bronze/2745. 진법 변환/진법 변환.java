import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// B진법 숫자 N
		Scanner sc = new Scanner(System.in);
		String n = sc.next();
		int b = sc.nextInt();

		long result = 0;
		int idx = 0;
		int num = 0;

		// 10진수로 바꿔서 사용
		for (int i = n.length() - 1; i >= 0; i--) {
			char c = n.charAt(i);
			// 0~9는 그대로 출력
			if (c >= '0' && c <= '9') {
				num = c - '0';
			} else {
				// A~Z는 숫자로 변경
				num = c - 55;
			}
			// 10진수 숫자*각 자리수 제곱을 모두 더한 값이 10진수
			result += num * Math.pow(b, idx++);
		}

		System.out.println(result);

		sc.close();

	}

}