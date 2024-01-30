package Search;

public class LinearSearch {
    public static int linearSearch(int[] List, int target) {
        for (int i = 0; i < List.length; i++) {
            if (List[i] == target) {
                return i + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] List = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        System.out.println(linearSearch(List, 5));
        System.out.println(linearSearch(List, 11));
    }
}
