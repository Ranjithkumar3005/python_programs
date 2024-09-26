public class dum {

    public static int solve(int N, int start, int finish, int[] ticketCost) {
        // Convert to zero-based index
        int startIndex = start - 1;
        int finishIndex = finish - 1;

        // Calculate clockwise cost
        int clockwiseCost;
        if (finishIndex >= startIndex) {
            clockwiseCost = sum(ticketCost, startIndex, finishIndex - 1); // Use finishIndex - 1
        } else {
            clockwiseCost = sum(ticketCost, startIndex, N - 1) + sum(ticketCost, 0, finishIndex - 1); // Use finishIndex
                                                                                                      // - 1
        }

        // Calculate anti-clockwise cost
        int antiClockwiseCost;
        if (startIndex >= finishIndex) {
            antiClockwiseCost = sum(ticketCost, finishIndex, startIndex - 1); // Use startIndex - 1
        } else {
            antiClockwiseCost = sum(ticketCost, finishIndex, N - 1) + sum(ticketCost, 0, startIndex - 1); // Use
                                                                                                          // startIndex
                                                                                                          // - 1
        }

        // Return the minimum cost
        return Math.min(clockwiseCost, antiClockwiseCost);
    }

    private static int sum(int[] ticketCost, int start, int end) {
        int total = 0;
        if (start <= end) {
            for (int i = start; i <= end; i++) {
                total += ticketCost[i];
            }
        } else {
            for (int i = start; i < ticketCost.length; i++) {
                total += ticketCost[i];
            }
            for (int i = 0; i <= end; i++) {
                total += ticketCost[i];
            }
        }
        return total;
    }

    public static void main(String[] args) {
        int N = 4;
        int start = 1;
        int finish = 3;
        int[] ticketCost = { 1, 2, 3, 4 };

        int result = solve(N, start, finish, ticketCost);
        System.out.println(result); // Output the minimum cost
    }
}
