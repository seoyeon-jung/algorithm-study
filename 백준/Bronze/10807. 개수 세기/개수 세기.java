import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int count = 0; // v 와 일치할시 +1
		int N = sc.nextInt();
		int[] arr = new int[N]; // 배열 생성, 길이는 N만큼

		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt(); // 배열에 입력한 정수들 넣어주기
		}

		int v = sc.nextInt(); // 일치하는 정수 v

		for (int j = 0; j < arr.length; j++) {
			if (v == arr[j]) {
				count++;
			}
		}
		System.out.println(count);

		sc.close();

	}

}
