import java.util.*;
import java.io.*;

public class Main{
	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		StringTokenizer st = new StringTokenizer(line, " ");
		double a = Integer.parseInt(st.nextToken());
		double b = Integer.parseInt(st.nextToken());
		System.out.println(a/b);
	}
}