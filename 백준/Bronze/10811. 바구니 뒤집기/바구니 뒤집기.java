import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); // n 개의 바구니
		int count = sc.nextInt(); // 시행 회수

		int temp = 0;

		int busket[] = new int[N];
		for (int i = 0; i < busket.length; i++) {
			busket[i] = i + 1;
		}

		for (int i = 0; i < count; i++) {
			int a = sc.nextInt() - 1;
			int b = sc.nextInt() - 1;

			while (a < b) {
				temp = busket[a];
				busket[a] = busket[b];
				busket[b] = temp;
				a++;
				b--;
			}
		}

		sc.close();

		for (int i = 0; i < busket.length; i++) {
			System.out.print(busket[i] + " ");
		}

	}

}
