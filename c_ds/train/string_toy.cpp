

#include <iostream>
#include <sstream>

std::vector<std::string> str_split(const std::string& str, const std::string& delimiters) {
  std::vector<std::string> tokens;
  std::size_t pos = 0;
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

void play_split(){
  std::string sample_string = "data_n000000000000007425123291988432074571777-n000000000000007425123291988457844375553_t1728818475006642425-t1728818476001441034_r2_s542_p7425123291988380534964225.bin";
  auto offset = 6;
  auto size = 38;
  auto parts = str_split(sample_string, "_-");
  for (auto i = 0; i < parts.size(); i++) {
      std::cout << "index:" << i << " "<< parts[i] << std::endl;
  }
  std::cout << "prior nonce:" <<  parts[7].substr(1, parts[7].size()-5) << std::endl;  
  std::cout << "-------------------" << std::endl;
}
void play_build_prod_string(){
  std::string sample_string = "local/ksw/trading.trades/acc_9_sp_1/replay/data_n000000000000007426897163722029954760704-n000000000000007426897163979753762324480_t1729232556009101265-t1729242555009427774_r10000_s2393847_p7426897163464288967327744.bin:acc_9_sp_1:data_n000000000000007426897163722029954760704-n000000000000007426897163979753762324480_t1729232556009101265-t1729242555009427774_r10000_s2393847_p7426897163464288967327744.bin";
  auto parts = str_split(sample_string, "/");
  std::stringstream ss;
  for (auto i = 0; i < parts.size(); i++) {
    if (i == parts.size() - 2) {
      continue;
    }
    ss << parts[i] ;
    if (i != parts.size()-1){
      ss << "/";
    }
  }
  std::cout << sample_string << std::endl;
  std::cout << ss.str() << std::endl;
}

void play_build_backup_string(){
  std::string sample_string = "local/ksw/trading.trades/acc_9_sp_1/data_n000000000000007426897163722029954760704-n000000000000007426897163979753762324480_t1729232556009101265-t1729242555009427774_r10000_s2393847_p7426897163464288967327744.bin:acc_9_sp_1:data_n000000000000007426897163722029954760704-n000000000000007426897163979753762324480_t1729232556009101265-t1729242555009427774_r10000_s2393847_p7426897163464288967327744.bin";
  auto parts = str_split(sample_string, "/");
  parts[parts.size() - 2] =  parts[parts.size() - 2] + "/backup" ;
  std::stringstream ss;
  for (auto i = 0; i < parts.size(); i++) {
    ss << parts[i];
    if (i != parts.size() - 1) {
      ss << "/";
    }
  }
  std::cout << sample_string << std::endl;
  std::cout << ss.str() << std::endl;
}

int main(int argc, char *argv[]) {
    play_split();
    play_build_backup_string();
    std::cout << "-------------------" << std::endl;
    play_build_prod_string();
    return 0;
}