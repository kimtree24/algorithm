import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String input = br.readLine();
        
        List<String> inputStuff = new ArrayList<>();
        
        for(int i = 0; i < input.length(); i++){
            inputStuff.add(input.substring(i));
        }
        
        Comparator<String> asce = (a,b)-> a.compareTo(b);
        
        Collections.sort(inputStuff, asce);
        
        for(int i = 0; i < inputStuff.size(); i++){
            System.out.println(inputStuff.get(i));
        }
            
        
    }
}