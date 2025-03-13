import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int kim = sc.nextInt();
        int lim = sc.nextInt();
        int round = 0;

        // 현재 홀수인 경우에는 현재 번호 / 2 + 1
        // 현재 짝수인 경우에는 현재 번호 / 2
        while (kim != lim) {
            kim = kim / 2 + kim % 2;
            lim = lim / 2 + lim % 2;
            round++;
        }

        sc.close();

        System.out.println(round);
    }

}