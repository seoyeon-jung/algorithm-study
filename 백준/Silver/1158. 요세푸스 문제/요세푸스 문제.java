import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        // N명의 사람들, 양의 정수 K
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int index = 0; // 현재 위치 변수
        ArrayList<Integer> list = new ArrayList<>(); // list 형식으로 N명 리스트화
        for(int i = 1; i <= N; i++) {
            list.add(i);
        }

        // print 형식: < >
        bw.write("<");

        while(list.size() > 1) {
            // k 더했을때 현재 인원수보다 커지는 경우 처음 인원으로 돌아간다
            index = index + (K-1) < list.size() ? index + (K-1) : (index+(K-1)) % list.size();
            bw.write(list.get(index) + ", "); // 제거 위치 저장
            list.remove(index);
        }

        bw.write(list.get(0) + ">"); // 마지막 남은 사람 + > 추력
        bw.flush();
        bw.close();
        br.close();
    }
}
