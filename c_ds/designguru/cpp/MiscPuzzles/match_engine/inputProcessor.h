#ifndef __INPUTPROCESSOR_H__
#define __INPUTPROCESSOR_H__

#include <iterator>
#include <map>
#include <memory>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <stdexcept>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <utility>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

class OrderBook;
class InputProcessor{
public:
    InputProcessor(OrderBook& orderBook):m_orderBook(orderBook){}
    void handleInput(std::string);
private:
    ModifyOrderPtr modifyOrder(std::vector<std::string> &paramlist);
    OrderPtr buysellOrder(OrderType, std::vector<std::string>& );
    OrderBook   &m_orderBook;
};

#endif // __INPUTPROCESSOR_H__