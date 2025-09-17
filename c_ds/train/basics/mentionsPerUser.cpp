#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

template <typename S, typename T>
S& operator<<(S& s, vector<T> data){
    s << "[";
    for ( auto val :data){
        s << val << ", ";
    }
    s << "]";
    return s;
}

class OffStruct {
public:
    OffStruct():ts(1), online(true){}
    int ts ;
    bool online ;
};
template <typename S>
S& operator<<(S& s, OffStruct data){
    s << "ts:" << data.ts << " online:" << (data.online? "true": "false") ;
    return s;
}
class Solution {
public:
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        sort( begin(events), end(events),
            [](auto e1, auto e2){ 
                auto e1ts =  atoi(e1[1].data()) ;
                auto e2ts = atoi(e2[1].data());
                if ( e1ts == e2ts){ 
                    if (e1[0].find("OFFLINE") != string::npos) return true;
                    else return false;
                }else{
                    return e1ts < e2ts;
                }
            }
        );
        vector<OffStruct> offStruct(numberOfUsers);
        cout << "\t offStruct:" << offStruct << endl;
        vector<int> mentions(numberOfUsers, 0);
        for (auto event : events){
            cout << "\t\t" << event << endl;
            if (event[0].find("MESSAGE") != string::npos){
                // process message
                if (event[2].find("HERE") != string::npos){
                    int eventTs = atoi(event[1].data());
                    for ( int index = 0; index < numberOfUsers; ++ index) {
                        if (!offStruct[index].online && eventTs >= offStruct[index].ts + 60)
                            offStruct[index].online = true;
                        if ( offStruct[index].online == true){
                            cout << "\t updating:" << index << endl;
                            mentions[index]++;
                        }
                    }
                }else if (event[2].find("ALL") != string::npos){
                    for ( int index = 0; index < numberOfUsers; ++ index) mentions[index]++;
                }else{ // this is the case for individual ids
                    string_view s(event[2].data(), event[2].length());
                    int current = 0;
                    while (current < s.length()){
                        auto space_offset = s.find(" ", current);
                        string_view index_str = s.substr(current+2, 1);
                        auto index = atoi(index_str.data());
                        mentions[index]++;
                        if (space_offset == string::npos) break;
                        current = space_offset + 1;
                    }
                }
            }else{
                int eventTs = atoi(event[1].data());
                int index = atoi(event[2].data());
                offStruct[index].ts = eventTs;
                offStruct[index].online = false;
            }
            cout << "\t offStruct:" << offStruct << endl;
        }
        return mentions;
    }
};

void test(){
    // vector<vector<string>> events{{"OFFLINE","10","0"},{"MESSAGE","12","HERE"}} ;
    // vector<vector<string>> events[["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]] ;
    vector<vector<string>> events{{"MESSAGE","2","HERE"},{"OFFLINE","2","1"},{"OFFLINE","1","0"},{"MESSAGE","61","HERE"}};
    Solution s;
    auto mentions = s.countMentions(3, events);
    cout << " mentions:" << mentions  << endl;
}
int main(){
    test();
    return 0;
}