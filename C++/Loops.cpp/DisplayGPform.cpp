#include<iostream>
using namespace std;

int main() {
    int n;
    
    cout << "Enter number of terms: ";
    cin >> n;
    int a=1;
    for(int i=1; i<=n; i++){
        cout << a << " ";
        a = a * 3;
    }
    cout << endl;
    
    return 0;
}