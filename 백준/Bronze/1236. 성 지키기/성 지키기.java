import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 세로 크기
        int M = sc.nextInt(); // 가로 크기
        int row = 0;
        int col = 0;

        // map 만들기
        char[][] map = new char[N][M];
        for(int i = 0; i < map.length; i++) {
            String str = sc.next();
            for(int j = 0; j < map[i].length; j++) {
                map[i][j] = str.charAt(j);
            }
        }

        // 행에 필요한 경비원 수
        for (int i = 0; i < N; i++) {
            boolean flag = true;
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 'X') {
                    flag = false;
                    break;
                }
            }
            if (flag) row++;
        }

        // 열에 필요한 경비원 수
        for (int i = 0; i < M; i++) {
            boolean flag = true;
            for (int j = 0; j < N; j++) {
                if (map[j][i] == 'X') {
                    flag = false;
                    break;
                }
            }
            if (flag) col++;
        }

        System.out.println(Math.max(row, col));
        sc.close();

    }
}
