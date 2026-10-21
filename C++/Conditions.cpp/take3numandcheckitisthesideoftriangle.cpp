#include<iostream>
using namespace std;

int main(){
    int a, b, c;
    //take 3 side of triangle
    cout << "enter 1st side: ";
    cin >>a;
    cout << "enter 2nd side : ";
    cin >>b;
    cout << "enter 3rd side; ";
    cin >>c;
//check if it is triangke or not
if((a+b)>c && (a+c)>b && (b+c)>a){
    cout << "it is a triangle";
}
else{
    cout << "it is not a triangle";
          }
   }
