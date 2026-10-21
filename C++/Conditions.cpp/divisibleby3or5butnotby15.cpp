#include<iostream>
using namespace std;

int main(){
    int n;
    cout << "Enter n : ";
    cin >> n;
    //check if n is divisible by 3 or 5 but not by 15
    if(n%5==0 && n%3==0){
        if(n%15!=0){
            cout << "divisible by 3 or 5 but not by 15";
                     }
          else{
            cout << "divisible by 3 or 5 and 15";
    
          }           
    }    

}