#include<stdio.h>
#include<conio.h>
int main();
    int percentage;
    printf("enter your percentage");
    scanf("%d",&percentage);
    if(percentage>=85)
    {
        printf("Grade A");
    }
    else if (percentage<=85 && percentage>=70)
    {
        printf("Gradde B");
    }
    else if (percentage<= && percentage>=50)
    {
        printf("Grade C");
    }
    else 
    {
        printf("Grade F");
    }
    getch();
