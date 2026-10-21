#include<iostream>
using namespace std;

int main() {
    int marks;
    
    cout << "Enter marks (0-100): ";
    cin >> marks;
    
    // Validate input
    if(marks < 0 || marks > 100) {
        cout << "Invalid marks! Please enter a number between 0 and 100" << endl;
        return 1;
    }
    
    // Grade calculation
    if(marks >= 80 && marks <= 100) {
        cout << "Grade: Very Good" << endl;
    }
    else if(marks > 61 && marks <= 80) {
        cout << "Grade: Good" << endl;
    }
    else if(marks > 41 && marks <= 61) {
        cout << "Grade: Average" << endl;
    }
    else {
        cout << "Grade: Fail" << endl;
    }
    
    return 0;
}