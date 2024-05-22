

#include <iostream>
#include <vector>

using namespace std;

typedef vector<pair<string, string>> Tags_t;

void call_with_tags_t();
void call_with_initializer_list();
void display_tags_t(Tags_t tags);

int main (){
    cout << "HW vector_use_learn" << endl;

    call_with_tags_t();
    cout << "now with initializer list" << endl;
    call_with_initializer_list();
    return 0;
}


void display_tags_t(Tags_t tags){
    for( auto val : tags){
        cout << val.first << ":" << val.second << endl;
    }
}
void call_with_tags_t(){
    Tags_t val ;
    val.push_back(make_pair("comp_id", "sample_1"));
    display_tags_t(val);
}
void call_with_initializer_list(){
    display_tags_t({{"comp_id", "sample_1"}});
}