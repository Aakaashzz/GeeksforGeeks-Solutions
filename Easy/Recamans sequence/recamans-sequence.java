//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
import java.lang.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            int n = Integer.parseInt(in.readLine());
            
            Solution ob = new Solution();
            ArrayList<Integer> ans = ob.recamanSequence(n);
            for(int i = 0;i < n;i++)
                System.out.print(ans.get(i)+" ");
            System.out.println();
        }
    }
}
// } Driver Code Ends

class Solution{
    static boolean isExists(int arr[],int c,int endIndex){
        for(int i =0; i <= endIndex; i++){
            if(c == arr[i])
                return true;
        }
        return false;
    }
    static ArrayList<Integer> recamanSequence(int n){
        // code here
        ArrayList<Integer> ls = new ArrayList<Integer>();
        int arr[] = new int[n];
        
        arr[0] = 0;
        ls.add(arr[0]);
        
        for(int i = 1; i < n; i++){
            int curr = arr[i-1]-i;
            // Check less than 0 or already exists in the sequence
            if(curr < 0 || isExists(arr,curr,i-1)){
                int ans = arr[i-1]+i;
                 arr[i] = ans;
            }
            else{
                arr[i] = curr;
            }
            ls.add(arr[i]);
        }
        return ls;
    }
}