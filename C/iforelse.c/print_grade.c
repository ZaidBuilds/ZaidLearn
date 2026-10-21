#include<stdio.h>
int main()
{
    int percentage;
    printf("enter the value of percentage :");
    scanf("%d",&percentage);
    if(percentage>=85)

    {
        printf("Grade A");
    }

    else if (percentage<85 && percentage>=70)
    {
        printf("grade B");
    }
    else if (percentage<70 && percentage>=50)
    {
        printf("Grade C");
    }
    else
    {
        printf("Grade F");
    }

    return 0;
}