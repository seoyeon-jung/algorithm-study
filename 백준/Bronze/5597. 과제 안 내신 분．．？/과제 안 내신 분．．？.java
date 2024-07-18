import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// 30명 (1번~30번 출석 번호)
		// 28명이 제출했고 제출 안 한 2명의 출석 번호를 구하는 프로그램
		Scanner sc = new Scanner(System.in);
		int[] numArr = new int[30];

		// 출석부 번호 들어온 곳을 1로 표시
		for (int i = 0; i < 28; i++) {
			int num = sc.nextInt();
			numArr[num - 1] = 1;
		}

		sc.close();

		// 출력: 출석 번호 중 작은 순서대로 출력
		for (int i = 0; i < numArr.length; i++) {
			if (numArr[i] != 1) {
				System.out.println(i + 1);
			}
		}

	}

}
