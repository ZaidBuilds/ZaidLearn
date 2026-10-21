#include<stdio.h>
int main()
{
    int i,n;
    printf("by for loop");
    printf("\n enter the value");
    scanf("%d",&n);
   printf("Multiplication table of %d:\n", n);

    for(i=1; i<=10; i++)
    {
        printf("%d * %d = %d\n",i,n,i*n);
    }
    return 0;
    
}