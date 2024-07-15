import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] nums = new int[10];
		int[] remains = new int[42]; // 나머지가 되는 경우의 수
		int count = 0;
		int num = 0;

		Arrays.fill(remains, 0);

		for (int i = 0; i < nums.length; i++) {
			nums[i] = sc.nextInt();
			num = nums[i] % 42;
			remains[num] = num + 1;
		}

		sc.close();

		for (int i = 0; i < remains.length; i++) {
			if (remains[i] != 0) {
				count++;
			}
		}

		System.out.println(count);

	}

}
