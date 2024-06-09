package Search;

public class BinarySearch {
    public int binarySearch(int[] list, int n, int start, int end) {
        if (start > end) {
            return -1; // Element not found
        }

        int mid = (start + end) / 2;
        int midElement = list[mid];

        if (midElement == n) {
            return mid;
        } else if (midElement > n) {
            return binarySearch(list, n, start, mid - 1);
        } else {
            return binarySearch(list, n, mid + 1, end);
        }
    }
}

class Main {
    public static void main(String[] args) {
        int[] list = {1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16};
        int n = 13;
        BinarySearch bs = new BinarySearch();
        int index = bs.binarySearch(list, n, 0, list.length - 1);
        System.out.println(index); // Output: 8 (index of element 13)
    }
}