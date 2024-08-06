import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static int n, m;
	public static boolean[] visit;
	public static int[] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		visit = new boolean[n];
		arr = new int[m];

		dfs(0);
		System.out.println(sb);

	}

	public static void dfs(int depth) {
		if (depth == m) {
			for (int num : arr) {
				sb.append(num).append(" ");
			}
			sb.append("\n");
			return;
		}

		for (int i = 0; i < n; i++) {
			// 방문하지 않은 경우
			if (!visit[i]) {
				visit[i] = true; // 해당 노드 방문상태 변경
				arr[depth] = i + 1; // 해당 깊이를 index로 지정
				dfs(depth + 1); // 다음 자식 노드 방문
				visit[i] = false; // 방문 완료
			}
		}
	}

}