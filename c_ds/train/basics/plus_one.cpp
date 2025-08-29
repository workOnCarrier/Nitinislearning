#include <iostream>
#include <vector>


using namespace std;
void display(const vector<int>& digits){
    cout << "(";
    for (auto v: digits){
        cout << v << ", ";
    }
    cout << ")" << endl;
}

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        auto digit_len = digits.size();
        int carry = 1;
        auto digit_pos = digit_len -1;
        while (digit_pos >= 0 && carry == 1 && digit_pos <= digit_len){
            auto new_carry = (digits[digit_pos] + carry) / 10;
            digits[digit_pos] = (digits[digit_pos] + carry) % 10;
            carry = new_carry;
            digit_pos--;
        }
        if (carry != 0){
            digits.insert(digits.begin(), carry);
        }
        return digits;
    }
};

int main (){
    vector<int> input_1{1,2,3};
    vector<int> input_2{9};
    vector<int> input_3{4, 3, 2, 1};
    Solution s;
    display(s.plusOne(input_1));
    cout << "\n" ;
    display(s.plusOne(input_2));
    cout << "\n" ;
    display(s.plusOne(input_3));
    vector<int> input_4(4, 0);
    display(input_4);

    return 0;
}