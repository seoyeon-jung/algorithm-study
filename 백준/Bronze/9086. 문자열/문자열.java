import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt(); // test case 개수
		for (int i = 0; i < T; i++) {
			String word = sc.next(); // 문자열 입력
			System.out.println(String.valueOf(word.charAt(0)) + String.valueOf(word.charAt(word.length() - 1)));
		}

		sc.close();

	}

}
