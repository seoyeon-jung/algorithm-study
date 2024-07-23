import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		int count = 0;

		for (int i = 0; i < N; i++) {
			if (checkStr(br.readLine())) {
				count++;
			}
		}
		br.close();
		System.out.println(count);
	}

	static boolean checkStr(String str) {
		// boolean 형 배열에 초기값을 주지 않으면 모두 false

		boolean[] checkAlpha = new boolean[26]; // 알파벳은 26개
		int prev = -1; // 이전 문자의 인덱스값 저장

		for (int i = 0; i < str.length(); i++) {
			int now = str.charAt(i); // 현재 문자의 아스키코드값 저장

			// 이전 문자와 i번째 문자가 같지 않다면
			if (prev != now) {
				// false라는 것은 문자가 처음 나온 문자라는 것!
				if (checkAlpha[now - 97] == false) {
					// 처음나왔음을 확인 했으니까 다음에 나오면 두번째로 나온 문자임으로 true로 변경
					checkAlpha[now - 97] = true;
					prev = now; // 이전 문자와 비교 해야하므로 다음 반복문때에는 지금 문자가 이전문자가 되니까 확인
				} else {
					// 이미 나온적이 있음
					return false; // 반복문 돌 필요 없응
				}
			} else {
				// 만약 이전 문자와 지금의 문자가 같다면 => 연속된 문자이므로 그냥 계속 반복문을 진행
				continue;
			}
		}
		return true;
	}

}