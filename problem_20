# Problem #20
# Find the sum of the digits in the number 100!.
# Solution using Java
# For understanding you can go to http://www.geeksforgeeks.org/factorial-large-number/.


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Main {
  
  public static int multiply(int x,int[] res ,int res_size){
    int carry = 0;
    
    for(int i=0;i<res_size;i++){
      int prod = res[i]*x + carry;
      res[i] = prod%10;
      carry = prod/10;
    }
    
    while(carry>0){
      res[res_size] = carry%10;
      carry = carry/10;
      res_size++;
    }
    return res_size;
  }
  
  public static void factorial(int n){
    int[] res = new int[200];
    res[0] = 1; int res_size = 1;
    
    for(int i=2;i<=n;i++){
      res_size = multiply(i,res,res_size);
    }
    
    int sum =0;
    for(int i=res_size-1;i>-1;i--){
      sum += res[i];
      System.out.print(res[i]);
    }
    System.out.println();
    System.out.println(sum);
  }
  
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    System.out.println("Enter the no.:");
    int t = s.nextInt();
    s.close();
    factorial(t);
  }
}
