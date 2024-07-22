import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		int[] arr = new int[26]; // 각 문자의 위치를 가리킬 배열
		for (int i = 0; i < arr.length; i++) {
			arr[i] = -1;
		}

		Scanner sc = new Scanner(System.in);
		String word = sc.nextLine();
		sc.close();

		for (int i = 0; i < word.length(); i++) {
			char ch = word.charAt(i);

			// arr 원소값이 -1인 경우 초기화
			if (arr[ch - 'a'] == -1) {
				arr[ch - 'a'] = i;
			}
		}

		for (int i : arr) {
			System.out.print(i + " ");
		}

	}

}
