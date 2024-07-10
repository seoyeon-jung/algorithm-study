import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 현재 시각 입력
		int this_H = sc.nextInt();
		int this_M = sc.nextInt();

		// 필요한 시간을 분 단위로 입력
		int waiting = sc.nextInt();

		int min = 60 * this_H + this_M;
		min += waiting;

		int hour = (min / 60) % 24;
		int minute = min % 60;

		System.out.println(hour + " " + minute);

		sc.close();
	}
}
