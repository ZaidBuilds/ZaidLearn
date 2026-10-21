#include<iostream>
using namespace std;

int main(){
    int number;
    cout << "Enter Number: ";
    cin >> number;
    if(number>99 && number<1000){
        cout << "three digit number";
    }
    else{
        cout << "not a three digit number";
    }
}