import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int X = Integer.parseInt(br.readLine());
		br.close();

		int squareCount = 1; // 해당 대각선에 있는 칸의 개수
		int squareSum = 0; // 해당 대각선의 전 대각선 칸을 누적 더해서 저장하는 변수

		while (true) {
			// 현재 해당하는 대각선에 해당 x번재 분수가 있을 때
			if (X <= squareSum + squareCount) {
				if (squareCount % 2 == 1) {
					// 개수가 홀수 -> 분자 감소, 분모 증가
					System.out.println((squareCount - (X - squareSum - 1) + "/" + (X - squareSum)));
					break;
				} else {
					// 개수가 짝수 -> 분자 증가, 분모 감소
					System.out.println((X - squareSum) + "/" + (squareCount - (X - squareSum - 1)));
					break;
				}
			} else {
				// 아직 x번째 분수가 해당 대각선에 포함되지 않는 경우
				squareSum += squareCount;
				squareCount++; // 대각선이 늘때마다 칸의 개수도 +1 늘기 때문
			}
		}

	}

}