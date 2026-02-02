#include <iostream>
#include <unordered_map>
#include <limits.h>

using namespace std;

class Solution {
public:
    string minWindow_(string s, string t) {
        unordered_map<char, int> tfreq, sfreq;
        for ( char tc : t){
            tfreq[tc]++;
            sfreq[tc] = 0;
        }
        int fl = 0, fr = 0, min_len = INT_MAX;
        int l  = 0, r = 0;
        int metcount = 0, reqcount = tfreq.size();
        while ( r < s.length() ){
            if ( sfreq.contains(s[r]) ) {
                sfreq[s[r]] += 1;
                if ( sfreq[s[r]] == tfreq[s[r]] ){
                    metcount += 1;
                }
            }
            while ( metcount == reqcount){
                cout << s.substr(l, r - l + 1) << " " << metcount << " " << s[l] << endl;
                if ( r - l + 1 < min_len){
                    fr = r;
                    fl = l;
                    min_len = r - l + 1;
                }
                if (sfreq.contains(s[l])){
                    cout <<  metcount << " " << sfreq[s[l]] << " " << l << ":" << r ;
                    sfreq[s[l]] -= 1;
                    if ( sfreq[s[l]] < tfreq[s[l]] ){
                        metcount -= 1;
                    }
                    cout <<  "\t" << metcount << endl ;
                }
                l += 1;
            }
            r += 1;
        }
        return s.substr(fl, min_len);
    }
    string minWindow(string s, string t) {
        unordered_map<char, int> tfreq, sfreq;
        for ( auto tc : t){
            tfreq[tc] += 1;
            sfreq[tc] = 0;
        }
        int fl = 0, fr = s.length() - 1;
        int l = 0;
        int metc = 0, reqc = tfreq.size();
        bool found = false;
        for ( auto r  = 0; r < s.length(); ++ r){
            auto c = s[r];
            if ( sfreq.contains(c) ){
                sfreq[c] += 1;
                if (sfreq[c] == tfreq[c]){
                    metc += 1;
                }
            }
            cout << "checking for " << c << endl;
            while (metc == reqc && l < s.length() ){
                found = true;
                cout << metc << " removing for " << l << " : " << s[l] << endl;
                if (sfreq.contains(s[l])){
                    if (fr - fl > r - l){
                        fr = r;
                        fl = l;
                    }
                    sfreq[s[l]] -= 1; 
                    if (sfreq[s[l]] < tfreq[s[l]]){
                        metc -= 1;
                    }
                }
                l += 1;
            }
        }
        cout << "found: " << found << " " << fr  << " : " << fl << endl;
        // return found ? s.substr(fl, fr - fl + 1) : "";
        return "";
    }
};


int main(){
    Solution sol;
    string s = "ADOBECODEBANC";
    string t = "ABC";
    auto result = sol.minWindow(s, t);
    cout << "final result: " << result.length() << "  " << result << endl;;
    return 0;
}