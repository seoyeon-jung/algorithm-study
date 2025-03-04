import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        PriorityQueue<Integer> queue = new PriorityQueue<>();

        // 연산 개수 N 입력
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());

            if (num == 0) {
                // x == 0 (배열에서 가장 작은 값 출력, 배열에서 제거)
                if (queue.isEmpty()) {
                    bw.write("0\n");
                }
                else {
                    // 자연수라면 x라는 값을 넣는 연산
                    bw.write(queue.poll()+"\n");
                }
            }
            else {
                // 연산에 대한 정보 X 입력
                queue.add(num);
            }
        }

        bw.flush();
        bw.close();
    }
}