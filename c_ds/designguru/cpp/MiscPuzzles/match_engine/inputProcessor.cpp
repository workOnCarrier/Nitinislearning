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

#include "inputProcess.h"

void InputProcessor::handleInput(std::string orderInput){
    std::cerr << orderInput << std::endl;
    std::istringstream orderParamStream(orderInput.data());
    std::vector<std::string> orderParamList((std::istream_iterator<std::string>(orderParamStream)), std::istream_iterator<std::string>());
    auto orderTypeString = orderParamList[0];
    if (orderTypeString == "BUY"){
        m_orderBook.processOrder( buysellOrder(OrderType::BUY, orderParamList));
    }else if (orderTypeString == "SELL"){
        m_orderBook.processOrder(buysellOrder(OrderType::SELL, orderParamList));
    } else if (orderTypeString == "CANCEL"){
        if (orderParamList.size() >= 2){
            std::string orderId = orderParamList[1];
            auto orderPtr = std::make_shared<Order>(orderId, OrderType::CANCEL);
            m_orderBook.processOrder(orderPtr);
        }
    }else if (orderTypeString == "MODIFY"){
        if (orderParamList.size() < 5){ return ; }
        m_orderBook.processModifyOrder(modifyOrder(orderParamList));
    }else if (orderTypeString == "PRINT"){
        m_orderBook.printOrderBook();
    }else{
       throw std::runtime_error("intput invalid -- supported are [BUY, SELL, CANCEL, MODIFY, PRINT ]");
    }
}
ModifyOrderPtr InputProcessor::modifyOrder(std::vector<std::string> &paramlist){
    std::string orderId = paramlist[1];
    OrderType orderType;
    if (paramlist[2] == "SELL"){
        orderType = OrderType::SELL;
    }else if (paramlist[2] == "BUY"){
        orderType = OrderType::BUY;
    }else{
        std::string error_msg = "expected BUY / SELL found";
        throw std::runtime_error(error_msg + paramlist[2]);
    }
    auto price = atoi(paramlist[3].data());
    auto quantity = atoi(paramlist[4].data());
    
    auto cancelOrderPtr = std::make_shared<Order>(orderId, OrderType::CANCEL);
    auto newOrderPtr = std::make_shared<Order>(orderId, orderType, PlaceOrderType::GFD, price, quantity);
    auto modifyOrder = std::make_shared<ModifyOrder>(cancelOrderPtr, newOrderPtr);
    return modifyOrder;
}
OrderPtr InputProcessor::buysellOrder(OrderType buysell, std::vector<std::string> &paramlist){
    PlaceOrderType placeOrderType;
    if (paramlist[1] == "IOC")placeOrderType = PlaceOrderType::IOC;
    else if (paramlist[1] == "GFD")placeOrderType = PlaceOrderType::GFD;
    else {
        std::string error_message = "invalid Place order type:" ;
        throw std::runtime_error(error_message + paramlist[1]);
    }
    int price = atoi(paramlist[2].data());
    int quantity = atoi(paramlist[3].data());
    auto orderPtr = std::make_shared<Order>(paramlist[4], buysell, placeOrderType, price, quantity);
    return orderPtr;
}