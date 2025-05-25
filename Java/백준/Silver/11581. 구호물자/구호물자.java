import java.util.*;
import java.io.*;

public class Main {
    static List<Integer>[] graph;
    static boolean isCycle = false;
    static int[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numCross = Integer.parseInt(br.readLine().trim());
        graph = new ArrayList[numCross + 1];

        for (int i = 1; i <= numCross; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i < numCross; i++) {
            String line = br.readLine();
            while (line != null && line.trim().isEmpty()) {
                line = br.readLine();
            }

            int m = 0;
            try {
                m = Integer.parseInt(line.trim());
            } catch (NumberFormatException e) {
                System.out.println("CYCLE");
                return;
            }

            if (m > 0) {
                line = br.readLine();
                while (line != null && line.trim().isEmpty()) {
                    line = br.readLine();
                }

                if (line == null) {
                    System.out.println("CYCLE");
                    return;
                }

                StringTokenizer st = new StringTokenizer(line);
                while (st.hasMoreTokens()) {
                    String token = st.nextToken();
                    try {
                        int nextCross = Integer.parseInt(token);
                        graph[i].add(nextCross);
                    } catch (NumberFormatException e) {
                        System.out.println("CYCLE");
                        return;
                    }
                }
            }
        }

        visited = new int[numCross + 1];
        dfs(1);

        System.out.println(isCycle ? "CYCLE" : "NO CYCLE");
    }

    public static void dfs(int node) {
        if (isCycle) return;
        visited[node] = 1;

        for (int next : graph[node]) {
            if (visited[next] == 0) {
                dfs(next);
            } else if (visited[next] == 1) {
                isCycle = true;
                return;
            }
        }

        visited[node] = 2;
    }
}