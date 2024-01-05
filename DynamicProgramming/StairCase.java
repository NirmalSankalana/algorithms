public class StairCase {
    public int move(int n) {
        // n: f(n-1) + f(n-2)

        if (n <= 1)
            return n;
        else if (n == 2)
            return 2;
        int result = move(n - 1) + move(n - 2);
        return result;
    }

    public static void main(String[] args) {
        StairCase s = new StairCase();
        System.out.println(s.move(10));
    }
}
