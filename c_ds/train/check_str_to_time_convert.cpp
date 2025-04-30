
#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <cstdint>
#include <stdexcept>


std::string sample_string = "data_n000000000000007425123291988432074571777-n000000000000007425123291988457844375553_t1728818475006642425-t1728818476001441034_r2_s542_p7425123291988380534964225.bin";

std::vector<std::string> str_split(const std::string& str, const std::string& delimiters) {
    std::vector<std::string> tokens;
    std::size_t  pos = 0;
    std::size_t found = str.find_first_of(delimiters, pos);

    while (found != std::string::npos) {
        if (found > pos) {
            tokens.push_back(str.substr(pos, found - pos));
        }
        pos = found + 1;
        found = str.find_first_of(delimiters, pos);
    }

    if (pos < str.size()) {
        tokens.push_back(str.substr(pos));
    }

    return tokens;
}

uint64_t split_time_uint64t(const std::string& start_ts_str) {
    try{
        uint64_t number = std::stoull(start_ts_str.substr(1));
        return number;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "Out of range: " << e.what() << std::endl;
    }
    return 0;
}


int main(int argc, char *argv[]) {

    std::vector<std::string> parts = str_split(sample_string, "_-");
    for ( auto part : parts ) {
        std::cout << part << std::endl;
    }
    auto timestamp = split_time_uint64t(parts[3]);
    std::cout << "timestamp: " << timestamp << " for value" << parts[3] << std::endl;
    timestamp = split_time_uint64t(parts[4]);
    std::cout << "timestamp: " << timestamp << " for value" << parts[4] << std::endl;

    std::cout << "Hello world!\n";
    return 0;
}