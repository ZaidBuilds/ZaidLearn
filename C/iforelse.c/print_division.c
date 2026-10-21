#include<stdio.h>
int main()
{
    int percentage;
    printf("enter the value of percentage :");
    scanf("%d",&percentage);
    if(percentage>=85)

    {
        printf("1st Division");
    }

    else if (percentage<85 && percentage>=70)
    {
        printf("2nd Division");
    }
    else if (percentage<70 && percentage>=50)
    {
        printf("3rd Division");
    }
    else
    {
        printf("4th Division");
    }

    return 0;
}