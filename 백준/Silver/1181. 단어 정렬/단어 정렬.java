import java.io.*;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] list = new String[N];
        for (int i = 0; i < N; i++) {
            list[i] = br.readLine();
        }

        // 길이가 짧은 것부터
        // 길이가 같으면 사전 순으로

        Arrays.sort(list, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.length() == s2.length()) {
                    return s1.compareTo(s2);
                } else {
                    return s1.length() - s2.length();
                }
            }
        });

        System.out.println(list[0]);
        for (int i = 1; i < N; i++) {
            if (!list[i].equals(list[i-1])) {
                System.out.println(list[i]);
            }
        }

    }
}