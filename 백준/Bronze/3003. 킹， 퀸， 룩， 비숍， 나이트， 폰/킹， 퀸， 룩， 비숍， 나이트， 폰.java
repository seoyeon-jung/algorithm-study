import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개 = 총 16개

		// 킹, 퀸, 룩, 비숍, 나이트, 폰 입력
		int[] inputArr = new int[6];
		for (int i = 0; i < inputArr.length; i++) {
			inputArr[i] = sc.nextInt();
		}

		int[] outputArr = new int[6];

		outputArr[0] = 1 - inputArr[0];
		outputArr[1] = 1 - inputArr[1];
		outputArr[2] = 2 - inputArr[2];
		outputArr[3] = 2 - inputArr[3];
		outputArr[4] = 2 - inputArr[4];
		outputArr[5] = 8 - inputArr[5];

		for (int i : outputArr) {
			System.out.print(i + " ");
		}

		sc.close();
	}
}
