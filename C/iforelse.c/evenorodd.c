#include<stdio.h>
int main()
{
    int number=0;
    printf("Enter the value of number :");
    scanf("%d",&number);
    if(number%2==0)

{
    printf("number is even ",number);
}
else 
{
    printf("number is odd ",number);
}

return 0;

}