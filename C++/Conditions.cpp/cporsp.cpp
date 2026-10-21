#include<iostream>
using namespace std;

int main() {
    int cp, sp;
    
    // Input cost price
    cout << "Enter cost price: ";
    cin >> cp;
    
    // Input selling price
    cout << "Enter selling price: ";
    cin >> sp;
    
    // Check for profit, loss or no profit no loss
    if(sp > cp) {
        cout << "Profit" << endl;
    }
    else if(sp < cp) {
        cout << "Loss" << endl;
    }
    else {
        cout << "No profit no loss" << endl;
    }
    
    return 0;
}