import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 다섯줄 입력 받기 (최소 1개, 최소 15개의 글자들)
		char[][] str = new char[5][15];
		String input = ""; // 입력받은 문자 그대로 출력

		for (int i = 0; i < str.length; i++) {
			input = sc.next();
			// 15개 문자 넣기
			for (int j = 0; j < input.length(); j++) {
				str[i][j] = input.charAt(j);
			}
		}

		// 세로로 한 줄씩 출력해야 한다
		// 공백없이 연속해서 출력
		for (int i = 0; i < 15; i++) {
			for (int j = 0; j < 5; j++) {
				// 빈 문자열이면 출력하지 않는다.
				if (str[j][i] == '\0') {
					continue;
				}
				System.out.print(str[j][i]);
			}
		}

	}

}
