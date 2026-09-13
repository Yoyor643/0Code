package Set_;

import java.util.Arrays;
import java.util.Collections;

public class TestArrays {
    public static void main(String[] args) {
        new TestArrays().sortTest();
    }

    private static void sortTest() {
        String[] arr = {"Y", "o", "y", "o", "r", "G", "g"};
        System.out.println(Arrays.toString(arr));
        System.out.println("==========排序");
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));

        Arrays.sort(arr, String.CASE_INSENSITIVE_ORDER);
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr, Collections.reverseOrder()); // 降序排列，而不是颠倒
        System.out.println(Arrays.toString(arr));

        Arrays.sort(arr, Collections.reverseOrder(String.CASE_INSENSITIVE_ORDER)); // 降序排序，不区分大小写
        System.out.println(Arrays.toString(arr));
    }

}
