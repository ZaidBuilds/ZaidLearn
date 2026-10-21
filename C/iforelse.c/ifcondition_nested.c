#include<stdio.h>
int main()
{
    int number=0;
    printf("Enter the value of number :");
    scanf("%d",&number);
    if(number==10)

    {
        printf("number is equal to 10 ");
    }

    else if (number==50)
    {
        printf("number is equal to 50");
    }

    else if (number==100)
    {
        printf("number is equal to 100");
    }

    else 
    {
        printf("number is not equal to 10, 50 and 100");
    }

    return 0;
}