#include <iostream>
#include <exception>
#include <cstdlib>
#include <execinfo.h>
#include <csignal>


/*
-------------------------------
SAMPLE EXECUTION EXAMPL
-------------------------------
Starting the program...
Custom terminate called: Uncaught exception!
Stack trace:
0   stack_trace                         0x000000010218aea8 _Z16print_stacktracev + 52
1   stack_trace                         0x000000010218b0a8 _Z16custom_terminatev + 44
2   libc++abi.dylib                     0x000000018ebd8710 _ZSt11__terminatePFvvE + 16
3   libc++abi.dylib                     0x000000018ebdbcdc __cxa_get_exception_ptr + 0
4   libc++abi.dylib                     0x000000018ebdbc84 _ZN10__cxxabiv1L12failed_throwEPNS_15__cxa_exceptionE + 0
5   stack_trace                         0x000000010218b0ec _Z19function_that_failsv + 64
6   stack_trace                         0x000000010218b158 main + 72
7   dyld                                0x000000018e8a0274 start + 2840
zsh: abort      ./stack_trace

*/

void print_stacktrace() {
    const int max_frames = 128;
    void* frames[max_frames];

    // Capture the call stack
    int frame_count = backtrace(frames, max_frames);

    // Get human-readable symbols for the stack
    char** symbols = backtrace_symbols(frames, frame_count);
    if (symbols) {
        std::cerr << "Stack trace:" << std::endl;
        for (int i = 0; i < frame_count; ++i) {
            std::cerr << symbols[i] << std::endl;
        }
        free(symbols);
    }else {
        std::cerr << "Failed to print stack trace" << std::endl;
    }

}

void custom_terminate() {
    std::cerr << "Custom terminate called: Uncaught exception!" << std::endl;
    print_stacktrace();
    abort();  // Ensure the program stops after printing the stack trace
}

void function_that_fails() {
    throw std::runtime_error("An exception that will lead to std::terminate");
}

int main() {
    // Set the custom terminate handler
    std::set_terminate(custom_terminate);
    std::cerr << "Starting the program..." << std::endl;

    // try {
        function_that_fails();
    // } catch (...) {
        // Intentionally do nothing, will result in std::terminate being called
    // }

    return 0;
}
