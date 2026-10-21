#include<iostream>
using namespace std;

int main() {
    int n;
    cout << "enter n : ";
    cin >> n;
    //check if n is even or odd
    (n%2==0)? cout << "even" : cout << "odd" ;
    return 0;
}