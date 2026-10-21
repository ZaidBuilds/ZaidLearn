#include<iostream>
using namespace std;

int main() {
    cout << "Printing odd numbers from 1 to 99:" << endl;
    
    for(int i = 1; i < 100; i++) {
        if(i % 2 == 0) {
            continue;  // Skip even numbers
        }
        cout << i << " ";  // Print odd numbers
    }
    cout << endl;
    
    return 0;
}