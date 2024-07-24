import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// 9X9 격자판에 쓰여진 81개 자연수 또는 0
		// 최댓값을 찾고 최댓값의 위치를 구하는 프로그램

		Scanner sc = new Scanner(System.in);

		int max = 0;
		int x = 1;
		int y = 1;

		int[][] numArr = new int[9][9];
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				numArr[i][j] = sc.nextInt();
			}
		}
		sc.close();

		// 최댓값 구하기
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (numArr[i][j] > max) {
					max = numArr[i][j];
					x = i + 1;
					y = j + 1;
				}
			}
		}

		System.out.println(max);
		System.out.println(x + " " + y);

	}

}