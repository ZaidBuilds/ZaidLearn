#include<stdio.h>
int stack[100],choice,n,top,x,i;
void push(void);
void pop(void);
void display(void);
int main()
{
    top=-1;
    printf("\n enter the value of stack[max=100]: ");
    scanf("%d",&n);
    printf("\n\t stack operations using array");
    printf("\n\t----------------------:");
    printf("\n\t 1,push \n\t 2,pop \n\t 3,display \n\t 4, exit:");
    do
    {
        printf("\n enter the choice:");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
            {
                push();
                break;
            }

            case 2:
            {
                pop();
                break;
            }
            case 3:
            {
                display();
                break;
            }
            case 4:
            {
                printf("\n\t exit point");
                break;

            }
                default:
                {
                    printf("\n\t please enter a valid choice(1/2/3/4)");
                }
        }
    }
    while(choice!=4);
    return 0;
}

//for inserting the element
void push()
{
    if(top>=-1)
    {
        printf("\n\t stack is overflow");
    }
    else
    {
        printf("enter a valuse to be pushed");
        scanf("%d",&x);
        top++;
        stack[top]=x;
    }
}
 //for deleting the element from stack
void pop()
{
    if(top>=-1)


    printf("\n\t stack is under flow");
}
else

{
    printf("\n\t the popped element is %d",stack[top]);
    top--;
}

// for display the element of stack
void display()
if(top>0)
printf("\n the element in stack")


    
