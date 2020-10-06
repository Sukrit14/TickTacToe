/*Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
Input...
Test cases T (range=1-110)
Size of array N (N>=1)
Array elements

Output...
Maximum sum of contguous sub-array.

Example
Input...
2
5
1 2 3 -2 5
4
-1 -2 -3 -4

Output...
9
-1*/
#include<stdio.h>
int maxSub(int arr[], int n) 
{ 
    int max = arr[0], max_i = 0; 
  
    for (int i=0; i<n; i++) 
    { 
        max_i = max_i + arr[i]; 
        if (max < max_i) 
            max = max_i; 
        if (max_i < 0) 
            max_i = 0; 
    }
    return max; 
} 
int main() 
{  
    int T;
    scanf("%d", &T);
    if(T>=1 && T<=110)
    {
        for(int j=1;j<=T;j++)
        {
            int n;
            scanf("%d", &n);
            if(n>=1)
            {
                int arr[n];
                for(int i=0;i<n;i++)
                    scanf("%d", &arr[i]);
            
                int x = maxSub(arr, n);
                printf("%d\n", x);
            }
        }
    }
    return 0;
} 