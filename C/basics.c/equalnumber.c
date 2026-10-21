#include<stdio.h>
#include<conio.h>
int main(){
    int number=0;
    printf("enter a number");
    scanf("%d",&number);
    if(number==0){
        printf("number is equal to 10");

    }else if (number==20){
        printf("number is equal to 20");
    }
    else if (number==50)
    {
        printf("number is equal to 50");
    }
    else 
    {
        printf("number is not equal to 10,20 and 50");
    }
    getch();
    return 0;
}