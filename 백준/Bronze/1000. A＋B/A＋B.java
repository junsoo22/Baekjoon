import java.io.*;                                                                          
 import java.util.*;          

public class Main {
    public static void main(String[] args) throws IOException {

        //1000
        BufferedReader rd=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(rd.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        System.out.println(a + b);



    }
}