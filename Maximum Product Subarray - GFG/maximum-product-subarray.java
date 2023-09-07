//{ Driver Code Starts
import java.io.*;
import java.util.*;

  public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        while (tc-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int[] arr = new int[n];
            String[] inputLine = br.readLine().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            System.out.println(new Solution().maxProduct(arr, n));
        }
    }
}

// } Driver Code Ends


class Solution {
    // Function to find maximum product subarray
    long maxProduct(int[] arr, int n) {
        long max=Integer.MIN_VALUE;
        long product=1;
        for(int i=0;i<n;i++){
            product*=arr[i];
            if(product>max){
                max=product;
            }
            if(product==0){
                product=1;
            }
        }
        product=1;
        for(int i=arr.length-1;i>=0;i--){
            product*=arr[i];
            if(product>max){
                max=product;
            }
            if(product==0){
                product=1;
            }
        }
        return max;
    }
}