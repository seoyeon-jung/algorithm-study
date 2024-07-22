import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String word = sc.next().toUpperCase(); // 단어 입력 (대문자로 출력하니까 대문자로 변경)
		sc.close();

		int[] count = new int[26]; // 알파벳은 26개

		for (int i = 0; i < word.length(); i++) {
			int num = word.charAt(i) - 'A';
			count[num]++;
		}

		int max = 0;
		char answer = '?'; // 개수가 동일하면 ? 출력하므로 default가 ?
		for (int i = 0; i < count.length; i++) {
			if (max < count[i]) {
				max = count[i];
				answer = (char) (i + 'A');
			} else if (max == count[i]) {
				answer = '?';
			}
		}

		System.out.println(answer);

	}

}