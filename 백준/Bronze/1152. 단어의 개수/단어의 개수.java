import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String sentence = sc.nextLine(); // 문자열
		sc.close();

		StringTokenizer word = new StringTokenizer(sentence, " ");
		System.out.println(word.countTokens());

	}

}
