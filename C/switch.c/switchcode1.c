#include<stdio.h>
int main()
{
    int number;
    printf("enter the value of number :");
    scanf("%d",&number);
    switch(number)
    {
    case 1:
         printf("number is equal to 10");
         break;

    case 2:
        printf("number is equal to 20");
        break;
        
    case 3:
        printf("number is equal to 50");
        break;
        
    case 4:
          printf("number is equal to 100");
          break;

          default:
          printf("number is not equal to 10,20,30,50,100");

        
    }
          return 0;

}