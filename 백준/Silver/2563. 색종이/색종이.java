import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 색종이의 수 입력
		int n = Integer.parseInt(br.readLine());

		int total = 0; // 검은 영역의 넓이

		// 색종이를 붙일 위치 입력 (색종이의 수만큼)
		// 1. [색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리]
		// 2. [색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리]
		boolean[][] arr = new boolean[101][101]; // 도화지 전체

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());

			// 영역을 하나씩 체크한 후 총 넓이에 더해주기
			for (int j = x; j < x + 10; j++) {
				for (int k = y; k < y + 10; k++) {
					if (!arr[j][k]) {
						arr[j][k] = true;
						total++;
					}
				}
			}
		}

		// 색종이를 붙인 위치 출력
		System.out.println(total);

	}

}