import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// 1을 걸려면 총 2초
		// 숫자 +1 마다 +1초 추가
		// 어떤 단어 = 각 알파벳에 해당하는 숫자를 걸어야 한다
		// 전화를 걸기 위한 최소 시간 구하기

		Scanner sc = new Scanner(System.in);

		String s = sc.nextLine();
		sc.close();

		int count = 0;
		int k = s.length();

		for (int i = 0; i < k; i++) {

			switch (s.charAt(i)) {

			case 'A':
			case 'B':
			case 'C':
				count += 3;
				break;

			case 'D':
			case 'E':
			case 'F':
				count += 4;
				break;

			case 'G':
			case 'H':
			case 'I':
				count += 5;
				break;

			case 'J':
			case 'K':
			case 'L':
				count += 6;
				break;

			case 'M':
			case 'N':
			case 'O':
				count += 7;
				break;

			case 'P':
			case 'Q':
			case 'R':
			case 'S':
				count += 8;
				break;

			case 'T':
			case 'U':
			case 'V':
				count += 9;
				break;

			case 'W':
			case 'X':
			case 'Y':
			case 'Z':
				count += 10;
				break;
			}
		}
		System.out.print(count);
	}

}
