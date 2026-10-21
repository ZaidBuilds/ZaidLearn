#include<stdio.h>
int main()
{
    int a,b,c,opr;
    printf("enter the value of a and b :");
    scanf("%d%d",&a, &b);
    printf("enter the value of opr");
      scanf("%d",&opr);
    switch(opr)
    {
        case 1:
        c=a+b;
        printf("%d",c);
        break;

        case 2:
        c=a-b;
        printf("%d",c);
        break;

        case 3:
        c=a*b;
        printf("%d",c);
        break;

        case 4:
        c=a%b;
        printf("%d",c);
        break;

        case 5:
        c=a/b;
        printf("%d",c);
        break;

        default:
        printf("none");

        

    }

    return 0;

}