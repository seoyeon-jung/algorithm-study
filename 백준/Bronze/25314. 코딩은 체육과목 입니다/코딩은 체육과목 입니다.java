import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		// N바이트 크기의 정수

		// long int => 4바이트 정수
		// long long int => 8바이트 정수
		// long 하나씩 더 붙일 때마다 4바이트씩 저장할 수 있는 공간이 늘어난다고 생각

		for (int i = 0; i < (N / 4); i++) {
			System.out.print("long ");
		}
		System.out.print("int");

		sc.close();

	}

}
