#include<iostream>
using namespace std;

int main() {
    int length, breadth;
    
    // Input length and breadth
    cout << "Enter length: ";
    cin >> length;
    
    cout << "Enter breadth: ";
    cin >> breadth;
    
    // Check for negative values
    if(length <= 0 || breadth <= 0) {
        cout << "Please enter positive values for length and breadth" << endl;
        return 1;
    }
    
    // Calculate area and perimeter
    int area = length * breadth;
    int perimeter = 2 * (length + breadth);
    
    // Compare area and perimeter
    if(area > perimeter) {
        cout << "Area (" << area << ") is greater than perimeter (" << perimeter << ")" << endl;
    }
    else if(area < perimeter) {
        cout << "Perimeter (" << perimeter << ") is greater than area (" << area << ")" << endl;
    }
    else {
        cout << "Area and perimeter are equal (" << area << ")" << endl;
    }
    
    return 0;
}