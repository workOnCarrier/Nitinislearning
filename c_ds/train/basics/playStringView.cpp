#include <string_view>
#include <ranges>
#include <iostream>
#include <deque>

using namespace std;

std::string processViewOnly(const std::string &pathStr){

    string_view path(pathStr.data(), pathStr.length());
    string result;
    size_t start = 0;
    while (start < path.size()) {
        size_t end = path.find('/', start);
        if (end == std::string_view::npos) {
            result += "/" ;
            result += path.substr(start);
        }
        if (end != start) // avoid empty segments from '//' or leading/trailing slash
            result += "/" ;
            result += path.substr(start, end - start);
        start = end + 1;
    }
    return result;
}

std::string processViewRanges(std::string_view &path){
    std::string result;
    for (auto seg : std::views::split(path, '/')) {
        std::string_view dir(&*seg.begin(), std::ranges::distance(seg));
        if (!dir.empty()){
            result += "/" ;
            result += dir;
        }
    }
    return result;
}

class Solution {
public:
    string simplifyPath(string path) {
        std::string_view workPath (path.data(), path.length());
        std::deque<string_view> intermediate_result;
        std::string result;
        for ( auto word: std::views::split(workPath, '/')){
            std::string_view dir(&*word.begin(), std::ranges::distance(word));
            if (!dir.empty()){
                if (dir == string_view("..")){
                    if (!intermediate_result.empty()) intermediate_result.pop_back();
                }else{
                    cout << "\t\t adding to stack:" << dir << endl;
                    intermediate_result.push_back(dir);
                }
            } // else this is coming from "//" so ignoreing
        }
        while (!intermediate_result.empty()){
            auto val = intermediate_result.front();
            result += "/";
            result += val;
            cout << "\t\t adding to final result:" << val << endl;
            intermediate_result.pop_front();
        }
        if (result.length() == 0){
            result = "/";
        }
       return result;
    }
};

void test_solution(){
    Solution s;
    std::string path = "usr/local/bin/../";
    auto result = s.simplifyPath(path);
    cout << "\t solution result:" << result << endl;
}
void test_viewRanges(){
    std::string_view path = "usr/local/bin/";
    auto result = processViewRanges(path);
    cout << "\t result:" << result << endl;
}
void test_viewOnly(){
    std::string path = "usr/local/bin//";
    auto result = processViewOnly(path);
    cout << "\t result:" << result << endl;
}


int main(){
    test_viewRanges();
    test_viewOnly();
    test_solution();
    return 0;
}