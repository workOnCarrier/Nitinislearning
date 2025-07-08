#ifndef __ORDER_H__
#define __ORDER_H__

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

enum class OrderType{
    BUY,
    SELL,
    CANCEL,
    MODIFY,
    PRINT
};

enum class PlaceOrderType{
    IOC,
    GFD,
    NOT_APPLICABLE
};

class Order{
public:
    Order(std::string orderId, OrderType orderType, PlaceOrderType placeOrderType = PlaceOrderType::NOT_APPLICABLE, int price = 0, int quantity = 0);
    ~Order();
    Order(const Order&) = delete;
    Order& operator=(Order&) = delete;
    
    bool isBuyOrder() const {return OrderType::BUY == m_orderType;}
    bool isSellOrder() const {return OrderType::SELL == m_orderType;}
    bool isCancelOrder() const {return OrderType::CANCEL == m_orderType;}
    bool isFullyMatched() const {return m_outstandingQuantity <= 0;}
    int quantity() const {return m_quantity;}
    int outstanding() const {return m_outstandingQuantity;}
    int price() const {return m_price;}
    std::string orderId() const {return m_orderId;}
    
    bool isMatchPossible(const Order&);
    bool isMatchPossible(const int);
    int getMatchPrice(const Order&);
    int getMatchQuantity(const Order&);
    void updateMatch(Order&);
    bool isResting() {return m_placeOrderType == PlaceOrderType::GFD;}
    void cancel();
    
    template<typename ostream>
    friend ostream& operator<<(ostream&, const Order&);
private:
    OrderType           m_orderType;
    PlaceOrderType      m_placeOrderType;
    int                 m_price;
    int                 m_quantity;
    int                 m_outstandingQuantity;
    std::string         m_orderId;
};
typedef std::shared_ptr<Order> OrderPtr;
template<typename ostream>
ostream& operator<<(ostream& stream, const Order& order){
    stream << order.m_orderId << " " ;
    stream << ((order.m_orderType == OrderType::BUY)?"BUY" : "SELL") << " ";
    stream << ((order.m_placeOrderType == PlaceOrderType::GFD)?"GFD" : (order.m_placeOrderType == PlaceOrderType::IOC)?"IOC" : "NOT APPLICABLE") << " ";
    stream << order.price() << " ";
    stream << order.quantity() << " ";
    stream << order.m_outstandingQuantity << " ";
    return stream;
}

class ModifyOrder{
public:
    ModifyOrder(OrderPtr cancelOrder, OrderPtr newOrder):m_cancelOrder(cancelOrder), m_newOrder(newOrder){}
    ModifyOrder(const ModifyOrder&) = delete;
    ModifyOrder& operator =(ModifyOrder&) = delete;
    
    OrderPtr getCancelOrder(){return m_cancelOrder;}
    OrderPtr getNewOrder(){return m_newOrder;}
private:
    OrderPtr m_cancelOrder;
    OrderPtr m_newOrder;
};
typedef std::shared_ptr<ModifyOrder> ModifyOrderPtr;

#endif // __ORDER_H__