#include <iostream>
#include <map>


using namespace std;


//int main(){
//    cout << "hello wordl" << endl;
//    return 0;
//}

template<typename map_type>
void print_map(std::string_view comment, const map_type& m)
{
    std::cout << comment;
    // Iterate using C++17 facilities
    for (const auto& [key, value] : m)
        std::cout << '[' << key << "] = " << value << "; ";
 
// C++11 alternative:
//  for (const auto& n : m)
//      std::cout << n.first << " = " << n.second << "; ";
//
// C++98 alternative:
//  for (std::map<std::string, int>::const_iterator it = m.begin(); it != m.end(); ++it)
//      std::cout << it->first << " = " << it->second << "; ";
 
    std::cout << '\n';
}
 
void map_erase_if_toy()
{
    // Create a map of three (string, int) pairs
    std::map<std::string, int> m{{"CPU", 10}, {"GPU", 15}, {"RAM", 20}};
 
    print_map("1) Initial map: ", m);
 
    // m["CPU"] = 25; // update an existing value
    {
      // std::erase_if(m, [](const auto& pair){ return pair.first == "CPU"; });
      m.insert_or_assign("CPU", 25);
    }
    m["SSD"] = 30; // insert a new value
    print_map("2) Updated map: ", m);
 
    // Using operator[] with non-existent key always performs an insert
    std::cout << "3) m[UPS] = " << m["UPS"] << '\n';
    print_map("4) Updated map: ", m);
 
    m.erase("GPU");
    print_map("5) After erase: ", m);
 
    std::erase_if(m, [](const auto& pair){ return pair.second > 25; });
    print_map("6) After erase: ", m);
    std::cout << "7) m.size() = " << m.size() << '\n';
 
    m.clear();
    std::cout << std::boolalpha << "8) Map is empty: " << m.empty() << '\n';
}

void map_find_toy(){

    // Create a map of three (string, int) pairs
    std::map<int, std::string> m{ {1, "CPU_1", }, {2, "CPU_2", }, {3, "CPU_3", }, {4, "CPU_4", }, {5, "CPU_5", }, {6, "CPU_6", },
        {7, "CPU_7", }, {8, "CPU_8", }, {9, "CPU_9", }, {10, "CPU_10", },
        };
 
    print_map("1) Initial map: ", m);
    auto checker =  [m](int check_val){
        const auto&it = m.find(check_val);
        if (it == m.end()) std::cout << "map does not contain " << check_val << "\n";
        else std::cout << "map contains" << check_val << "\n";
    };
    checker(3);
    checker(4);
    checker(14);
    std::cout << "\n" ;
}

void map_upper_bound_lower_bound_toy(){

    // Create a map of three (string, int) pairs
    std::map<int, std::string> m{ {1, "CPU_1", }, {2, "CPU_2", }, {3, "CPU_3", }, {4, "CPU_4", }, {5, "CPU_5", }, {6, "CPU_6", },
        {7, "CPU_7", }, {8, "CPU_8", }, {9, "CPU_9", }, {10, "CPU_10", },
        };
 
    print_map("1) Initial map: ", m);
    try{
    for (auto iter = m.lower_bound(5);
             iter != m.upper_bound(7); iter++) {
          std::cout << (iter->second) << " ";
        }
    }catch(...){
        std::cout << "found exception" << "\n";
    }
    std::cout << "\n" ;
}

void map_upper_bound_lower_bound_toy_2(){

    // Create a map of three (string, int) pairs
    std::map<int, std::string> m{ {1, "CPU_1", }, {2, "CPU_2", }, {3, "CPU_3", } };
 
    print_map("1) Initial map: ", m);
    try{

    for (auto iter = m.upper_bound(3);
             iter != m.lower_bound(1); iter--) {
          std::cout << (iter->second) << " ";
        }
        cout << "\n";
    for (auto iter = m.lower_bound(1);
             iter != m.upper_bound(3); iter++) {
          std::cout << (iter->second) << " ";
        }
    }catch(...){
        std::cout << "found exception" << "\n";
    }
    std::cout << "\n" ;
}


int main(){
    // map_erase_if_toy();
    // map_upper_bound_lower_bound_toy();
    map_upper_bound_lower_bound_toy_2();
    // map_find_toy();
    return 0;
}