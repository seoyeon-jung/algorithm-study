import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1부ㅌ터 N까지 최소 개수 방 지나쳐 갈 때 몇 개 지나가는 지

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        br.close();

        int room = 1; // 찾을 방 최소 루트
        int findRoom = 2; // 최소 루트 (기본값)

        if (N == 1) {
            System.out.println(room);
        } else {
            while (findRoom <= N) {
                findRoom = findRoom + (6 * room);
                room++;
            }
            System.out.println(room);
        }

    }
}