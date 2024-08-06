import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			int n = Integer.parseInt(br.readLine());
			int count = 0;

			boolean[] isPrime = new boolean[(2 * n) + 1];

			// 0 입력시 무한루프 종료
			if (n == 0)
				break;

			// 0과 1은 소수가 아니다
			isPrime[0] = isPrime[1] = true;

			// 소수 판별하기
			for (int i = 2; i * i <= 2 * n; i++) {
				if (!isPrime[i]) {
					for (int j = i * i; j <= 2 * n; j += i) {
						isPrime[j] = true;
					}
				}
			}

			// count에 추가
			for (int i = n + 1; i <= 2 * n; i++) {
				if (!isPrime[i])
					count++;
			}

			System.out.println(count);
		}
	}

}
