#include <iostream>
#include <typeinfo>
#include <cxxabi.h> // Add this header for demangling

using std::cout ;
using std::endl ;

class Test {
public:
Test(){} // will not work without this def
Test(const Test& obj) {}
};

int main() {
    auto val = sizeof("test");
    const char* mangled = typeid("test").name();

    int status;
    char* demangled = abi::__cxa_demangle(mangled, nullptr, nullptr, &status);

    cout << "sizeof :" << val << endl;
    cout << "typeof (mangled): " << mangled << endl;
    if (status == 0 && demangled) {
        cout << "typeof (demangled): " << demangled << endl;
        free(demangled); // Don't forget to free the memory!
    } else {
        cout << "typeof (demangled): <demangling failed>" << endl;
    }

    Test t;
    return 0;
}
