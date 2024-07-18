import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int busket = sc.nextInt();
		int count = sc.nextInt();

		int n1, n2, temp = 0;

		int array1[] = new int[busket];

		for (int i = 0; i < array1.length; i++) {
			array1[i] = i + 1; // 바구니 초기 값
		}

		for (int i = 0; i < count; i++) {
			n1 = sc.nextInt() - 1;
			n2 = sc.nextInt() - 1;

			temp = array1[n1]; // temp에 'n1번째 바구니 값' 저장
			array1[n1] = array1[n2]; // n1번째 바구니에 'n2번째 바구니 값' 저장
			array1[n2] = temp; // n2번째 바구니에 temp('n1번째 바구니 값')저장

		}

		sc.close();

		for (int i = 0; i < array1.length; i++) {
			System.out.print(array1[i] + " ");
		}

	}

}
