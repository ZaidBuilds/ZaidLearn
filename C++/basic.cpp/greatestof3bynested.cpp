#include<iostream>
using namespace std;

int main(){
    int a, b, c;
    cout << "enter 1st number : ";
    cin >> a;
    cout << "enter 2nd number : ";
    cin >> b;
    cout << "enter 3rd number : ";
    cin >> c;
    //check if a is greater than b and c 
    if((a>b)){
        if((a>c)){
            cout << a << " is greater";
        }
    }
        else{
            if((b>c)){
                cout << b << " is greater";
            }
            else{
                cout << c << " is greater";
            }
        }

    }          
