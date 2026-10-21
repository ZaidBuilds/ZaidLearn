#include<stdio.h>

void printHello();

int main(){
    printHello();
    printBye();
    return 0;
}

void printHello(){
    print("Hello\n");
}

void printBye(){
    print("Bye\n");
}