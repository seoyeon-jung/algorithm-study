import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // 10진법 수
		int B = sc.nextInt(); // 진법

		List<Character> list = new ArrayList<>();
		while (N > 0) {
			if (N % B < 10) {
				list.add((char) (N % B + '0'));
			} else {
				list.add((char) (N % B - 10 + 'A'));
			}
			N /= B;
		}

		for (int i = list.size() - 1; i >= 0; i--) {
			System.out.print(list.get(i));
		}

		sc.close();
	}

}
