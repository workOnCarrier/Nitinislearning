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

#include "order.h"


Order::Order(std::string orderId, OrderType orderType, PlaceOrderType placeOrderType, int price, int quantity):
    m_orderType(orderType), m_placeOrderType(placeOrderType), m_price(price), m_quantity(quantity), m_outstandingQuantity(quantity), m_orderId(orderId){}
Order::~Order(){
    std::cerr << "\t destroying order:" << *this << std::endl;
}

bool Order::isMatchPossible(const Order& otherOrder){
    std::cerr << "\t check match:" << *this << "\t other:" << otherOrder << std::endl;
    if (isBuyOrder() == otherOrder.isBuyOrder()){
        throw std::runtime_error("This order matches the other orcer in side: incompatible match");
    }
    return isMatchPossible(otherOrder.price());
}
bool Order::isMatchPossible(const int otherPrice){
    if (isBuyOrder()){
        return otherPrice <= this->m_price && m_outstandingQuantity > 0;
    }else{
        return otherPrice >= this->m_price && m_outstandingQuantity > 0;
    }
}
int Order::getMatchPrice(const Order& other){
    if (!isMatchPossible(other.m_price)){
        throw std::runtime_error("attempting to get match price for mismatching orders");
    }
    return other.m_price;
}
int Order::getMatchQuantity(const Order& other){
    if (m_outstandingQuantity >= other.m_outstandingQuantity) return other.m_outstandingQuantity;
    return m_outstandingQuantity;
}
void Order::updateMatch(Order& other){
    if (m_outstandingQuantity > other.m_outstandingQuantity){
        m_outstandingQuantity = m_outstandingQuantity - other.m_outstandingQuantity;
        other.m_outstandingQuantity = 0;
    }else if (m_outstandingQuantity < other.m_outstandingQuantity){
        m_outstandingQuantity = 0;
        other.m_outstandingQuantity = other.m_outstandingQuantity - m_outstandingQuantity;
    }else{
        other.m_outstandingQuantity = 0;
        m_outstandingQuantity = 0;
    }
}
void Order::cancel(){
    m_outstandingQuantity = 0;
}

