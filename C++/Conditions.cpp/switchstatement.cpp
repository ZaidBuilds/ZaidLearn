#include<iostream>
using namespace std;

int main() {
    int n1, n2;
    char op;
    
    // Input first number
    cout << "Enter first number: ";
    cin >> n1;
    
    // Input operator
    cout << "Enter operator (+, -, *, /): ";
    cin >> op;
    
    // Input second number
    cout << "Enter second number: ";
    cin >> n2;
    
    // Check for division by zero
    if(op == '/' && n2 == 0) {
        cout << "Error: Division by zero is not allowed!" << endl;
        return 1;
    }
    
    // Perform calculation based on operator
    switch(op) {
        case '+':
            cout << n1 << " + " << n2 << " = " << n1 + n2 << endl;
            break;
            
        case '-':
            cout << n1 << " - " << n2 << " = " << n1 - n2 << endl;
            break;
            
        case '*':
            cout << n1 << " * " << n2 << " = " << n1 * n2 << endl;
            break;
            
        case '/':
            cout << n1 << " / " << n2 << " = " << n1 / n2 << endl;
            break;
            
        default:
            cout << "Invalid operator! Please use +, -, *, or /" << endl;
            break;
    }
    
    return 0;
}
