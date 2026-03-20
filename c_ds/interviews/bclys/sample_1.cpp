/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <vector>
/*
 
1. read line from console
 
2. count alphabets in input
 
Ex: aabbnbcdA
output
     a : 3
     b : 3
     c : 1
     d : 1
     n : 1
----
aaabbbbaaaaccc
b = 4

aaabbaaaaccc
a = 4

aaabbaaccaaaa

*/

using namespace std;
int sample_2(){
    std::string input;
    // pair -- first == size, second == starting position
    // std::vector<pair<int, int>> dist(26,std::make_pair(0,0)); // expected to initialize vector with all 26 pais as 0,0
    std::cin >> input;
    pair<int, int> cur;
    pair<int, int> cur_max;
    auto get_offset = [](char a) {return tolower(a) -'a';};
    for(int i = 0; i < input.length(); ++ i){
        if (i == 0){
            cur.first = 1;
            cur.second = 0;
        }else{
            if (input[i-1] == input[i]){ // we repition -- we increment existing value
                cur.first += 1;
            }else{ // new seq .. save the prev setup if greater than dist else discard
                auto cur_char = input[cur.second];
                if (cur_max.first < cur.first){
                    cur_max.first = cur.first;
                    cur_max.second = cur.second;
                }// else {}
                cur.first = 1;
                cur.second = i;
            }
        }
    }
    auto cur_char = input[cur.second];
    if (cur_max.first < cur.first){
        cur_max.first = cur.first;
        cur_max.second = cur.second;
    }// else {}
    cout << input[cur_max.second] << " : " << cur_max.first << endl;
    
    return 0;
}

int main(){
    return sample_2();
}

int sample_1 () {
    std::string val;
    std::vector<int> dist(26, 0);
    std::cin >> val ;
    for (auto &a: val) {
        auto la = std::tolower(a) - 'a';
        dist[la] += 1;
    }
    for (int i = 0; i < dist.size(); ++i ){
        if (dist[i] ==0) continue;
        cout << char('a' + i) << " : " << dist[i] << endl;
    }
    return 0;
}