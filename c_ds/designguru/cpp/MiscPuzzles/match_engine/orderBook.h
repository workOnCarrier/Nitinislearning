#ifndef __ORDERBOOK_H__
#define __ORDERBOOK_H__
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
#include "TradeHandler.h"

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
class SamePriceOrders{
public:
    SamePriceOrders(OrderPtr& order):m_price(order->price()), m_orderQueue(){m_orderQueue.push_back(order);}
    int getPrice()const {return m_price;}
    std::deque<OrderPtr>& getOrderQueue(){return m_orderQueue;}
    template<typename ostream>
    friend ostream& operator<<(ostream& stream, const SamePriceOrders& ordreQueu);
private:
    int m_price;
    std::deque<OrderPtr> m_orderQueue;
};
typedef std::shared_ptr<SamePriceOrders> SamePriceOrdersPtr;
template<typename ostream>
ostream& operator<<(ostream& stream, const SamePriceOrders& orderQueue){
    for (auto pos = orderQueue.m_orderQueue.begin(); pos != orderQueue.m_orderQueue.end(); pos++){
        std::cerr << "\t " << *pos ;
    }
    std::cerr << std::endl;
    return stream;
}

class OrderCompareAsc{
public:
    bool operator()(const SamePriceOrdersPtr left, const SamePriceOrdersPtr right){
        if (left->getPrice() <= right->getPrice()) return true;
        return false;
    }
};

class OrderCompareDesc{
 public:
    bool operator()(const SamePriceOrdersPtr left, const SamePriceOrdersPtr right){
        if (left->getPrice() >= right->getPrice()) return true;
        return false;
    }   
};

typedef std::priority_queue<SamePriceOrdersPtr, std::vector<SamePriceOrdersPtr>, OrderCompareAsc> BuyOrderQueue;
typedef std::priority_queue<SamePriceOrdersPtr, std::vector<SamePriceOrdersPtr>, OrderCompareDesc> SellOrderQueue;

class OrderBook{
public:
    OrderBook(TradeHandler& tradeHandler):m_tradeHandler(tradeHandler){}
    void processOrder(OrderPtr orderPtr);
    void processModifyOrder(ModifyOrderPtr orderPtr);
    void printOrderBook();
    void debugOrderBook();
private:
    void processOrderBuy(OrderPtr orderPtr);
    void processOrderSell(OrderPtr orderPtr);
    bool processCancelOrder(OrderPtr orderPtr);
    void addSellOrder(OrderPtr orderPtr);
    void addBuyOrder(OrderPtr orderPtr);
    void generateTrade(OrderPtr aggressor, OrderPtr resting);
    
    template<typename T, typename PriceQueueMap, typename OrderIdOrderMa>
    void matchOutstanding(OrderPtr orderPtr, T& priorityOrderQueue, PriceQueueMap& priceQueueMap, OrderIdOrderMa&);
    
    template<typename T, typename PriceQueueMap, typename OrderIdOrderMap>
    void removeOrder(std::string orderId, T& priorityOrdeQueue, PriceQueueMap &priceQueueMap, OrderIdOrderMap &orderIdOrderMap);
    
    std::unordered_map<int, SamePriceOrdersPtr> m_buyPriceQueueMap;
    std::unordered_map<int, SamePriceOrdersPtr> m_sellPriceQueueMap;
    std::unordered_map<std::string, OrderPtr>   m_sellOrderIdOrderMap;
    std::unordered_map<std::string, OrderPtr>   m_buyOrderIdOrderMap;
    BuyOrderQueue                               m_buyQueue;
    SellOrderQueue                              m_SellQueue;
    TradeHandler                                m_tradeHandler;
};
template<typename T, typename PriceQueueMap, typename OrderIdOrderMap>
void OrderBook::removeOrder(std::string orderId, T& priorityOrdeQueue, PriceQueueMap &priceQueueMap, OrderIdOrderMap &orderIdOrderMap){
    OrderPtr orderPtr = orderIdOrderMap[orderId];
    orderIdOrderMap.erase(orderId);
    SamePriceOrdersPtr queue = priceQueueMap[orderPtr->price()];
    auto& orderQueue = queue->getOrderQueue();
    std::cerr << "\t 0. removing order:" << *orderPtr << " \n\t from queue:" << *queue << std::endl;
    for (auto pos = orderQueue.begin(); pos != orderQueue.end(); pos++){
        if ((*pos)->orderId() == orderId){
            std::cerr << "\t 1. removing order:" << orderId << ":" << **pos << std::endl;
            orderQueue.erase(pos);
            break;
        }
    }
    std::cerr << "\t 2. after removing order:" << orderId << " \n\t from queue:" << *queue << std::endl;
    if (orderQueue.empty()){
        std::cerr << "\t 3. after attempting to remove empty queue:" <<  std::endl;
        priceQueueMap.erase(orderPtr->price());
    }
}
bool OrderBook::processCancelOrder(OrderPtr orderPtr){
    std::cerr << "\t cancelling:" << *orderPtr << std::endl;
    auto orderId = orderPtr->orderId();
    auto buyPresence = m_buyOrderIdOrderMap.find(orderId);
    if (buyPresence != m_buyOrderIdOrderMap.end()){
        removeOrder(orderId, m_buyQueue, m_buyPriceQueueMap, m_buyOrderIdOrderMap);
        return true;
    }
    auto sellPresence = m_sellOrderIdOrderMap.find(orderId);
    if (sellPresence != m_sellOrderIdOrderMap.end()){
        removeOrder(orderId, m_SellQueue, m_sellPriceQueueMap, m_sellOrderIdOrderMap);
        return true;
    }
    return false;
}

void OrderBook::debugOrderBook(){
        std::cerr << "\tSELL:" << std::endl;
        for (auto& keyVal: m_sellPriceQueueMap) {
            std::cerr << "\t"<<  keyVal.second->getPrice() << " ";
            int totalQuantity = 0;
            for (auto orderPtr : keyVal.second->getOrderQueue()){
                totalQuantity += orderPtr->outstanding();
                std::cerr << *orderPtr << std::endl;
            }
        }
        std::cerr  << "\tBUY:" << std::endl;
        for(auto& keyVal: m_buyPriceQueueMap){
            std::cerr << "\t" << keyVal.second->getPrice() << " ";
            int totalQuantity = 0;
            for(auto orderPtr: keyVal.second->getOrderQueue()){
                totalQuantity += orderPtr->outstanding();
                std::cerr << *orderPtr << std::endl;
            }
        }
}
void OrderBook::printOrderBook(){
        std::cout << "SELL:" << std::endl;
        std::map<int, int> sell_map;
        for (auto& keyVal: m_sellPriceQueueMap) {
            int totalQuantity = 0;
            for (auto orderPtr : keyVal.second->getOrderQueue()){
                totalQuantity += orderPtr->outstanding();
            }
            if (totalQuantity == 0) continue;
            sell_map[keyVal.first] = totalQuantity;
        }
        for ( auto skeyVal =  sell_map.rbegin(); skeyVal != sell_map.rend(); skeyVal++){
            std::cout << skeyVal->first << " " << skeyVal->second << std::endl;
        }
        std::cout  << "BUY:" << std::endl;
        
        std::map<int, int> buy_map;
        for(auto& keyVal: m_buyPriceQueueMap){
            int totalQuantity = 0;
            for(auto orderPtr: keyVal.second->getOrderQueue()){
                totalQuantity += orderPtr->outstanding();
            }
            if (totalQuantity == 0) continue;
            buy_map[keyVal.first] = totalQuantity;
        }
        for ( auto skeyVal =  buy_map.rbegin(); skeyVal != buy_map.rend(); skeyVal++){
            std::cout << skeyVal->first << " " << skeyVal->second << std::endl;
        }
 
}

Order::Order(std::string orderId, OrderType orderType, PlaceOrderType placeOrderType, int price, int quantity):
    m_orderType(orderType), m_placeOrderType(placeOrderType), m_price(price), m_quantity(quantity), m_outstandingQuantity(quantity), m_orderId(orderId){}
Order::~Order(){
    std::cerr << "\t destroying order:" << *this << std::endl;
}
void OrderBook::processOrder(OrderPtr orderPtr){
    if (orderPtr->isBuyOrder()){
        processOrderBuy(orderPtr);
    }else if (orderPtr->isSellOrder()){
        processOrderSell(orderPtr);
    }else if (orderPtr->isCancelOrder()){
        processCancelOrder(orderPtr);
    }// else if (orderPtr->isModifyOrder()){ processModifyOrder(orderPtr); } // invoked directly
    else{
        throw std::runtime_error("Order type is not handled");
    }
}
void OrderBook::processOrderBuy(OrderPtr orderPtr){
    matchOutstanding(orderPtr, m_SellQueue, m_sellPriceQueueMap, m_sellOrderIdOrderMap);
    if (!orderPtr->isFullyMatched() && orderPtr->isResting()) addBuyOrder(orderPtr);
}
void OrderBook::processOrderSell(OrderPtr orderPtr){
    // debugOrderBook();
    matchOutstanding(orderPtr, m_buyQueue, m_buyPriceQueueMap, m_buyOrderIdOrderMap);
    if (!orderPtr->isFullyMatched() && orderPtr->isResting()) addSellOrder(orderPtr);
    // debugOrderBook();
}
void OrderBook::processModifyOrder(ModifyOrderPtr modifyOrd){
    auto orderToCancel = modifyOrd->getCancelOrder();
    if (processCancelOrder(orderToCancel)){
        auto newOrder = modifyOrd->getNewOrder();
        processOrder(newOrder);
    }else{
        throw std::runtime_error("Modify failed because the original order is not found -- either it is not booked or it is already filled");
    }
}


void OrderBook::addSellOrder(OrderPtr orderPtr){
    std::cerr << "\t adding sell order:" << *orderPtr << std::endl;
    auto key = orderPtr->price();
    auto keyref = m_sellPriceQueueMap.find(key);
    if (keyref == m_sellPriceQueueMap.end()){
        auto priceOrderQueue = std::make_shared<SamePriceOrders>(orderPtr);
        m_sellPriceQueueMap.insert(std::make_pair(key, priceOrderQueue));
        m_SellQueue.push(priceOrderQueue);
    } else {
        auto sellQueue = keyref->second;
        sellQueue->getOrderQueue().push_back(orderPtr);
    }
    m_sellOrderIdOrderMap.insert(std::make_pair(orderPtr->orderId(), orderPtr));
    debugOrderBook();
}

void OrderBook::addBuyOrder(OrderPtr orderPtr){
    std::cerr << "\t adding buy order:" << *orderPtr << std::endl;
    auto key = orderPtr->price();
    auto keyref = m_buyPriceQueueMap.find(key);
    if (keyref == m_buyPriceQueueMap.end()){
        auto priceOrderQueue = std::make_shared<SamePriceOrders>(orderPtr);
        m_buyPriceQueueMap.insert(std::make_pair(key, priceOrderQueue));
        m_buyQueue.push(priceOrderQueue);
    }else{
        auto buyQueue = keyref->second;
        buyQueue->getOrderQueue().push_back(orderPtr);
    }
    m_buyOrderIdOrderMap.insert(std::make_pair(orderPtr->orderId(), orderPtr));
    debugOrderBook();
}

void OrderBook::generateTrade(OrderPtr aggressor, OrderPtr resting){
    if (aggressor->isFullyMatched() || resting->isFullyMatched()) {
        std::cerr << "\t Trade matching is broken" << std::endl;
    }
    std::cerr << "\t TRADE a:" << *aggressor << "\tr:" << *resting << std::endl;
    int tradePrice = aggressor->getMatchPrice(*resting);
    int tradeQuantity = aggressor->getMatchQuantity(*resting);
    aggressor->updateMatch(*resting);
    auto trade = std::make_shared<Trade>(aggressor, resting, tradePrice, tradeQuantity);
    m_tradeHandler.submitTrade(trade);
}

template<typename T, typename PriceQueueMap, typename OrderIdOrderMap>
void OrderBook::matchOutstanding(OrderPtr orderPtr, T& priorityOrderQueue, PriceQueueMap& priceQueueMap, OrderIdOrderMap &orderIdOrdermap){
    std::cerr << "\t matching:" << *orderPtr << std::endl;
    while(!priorityOrderQueue.empty() && !orderPtr->isFullyMatched()) {
        // std::cerr << "\t 1: matching in loop:" <<  std::endl;
        auto topPriceOrders = priorityOrderQueue.top();
        // std::cerr << "\t 2: matching in loop:" << topPriceOrders->getPrice() <<  std::endl;
        if ( orderPtr->isMatchPossible(topPriceOrders->getPrice())){
            auto& orderQueue = topPriceOrders->getOrderQueue();
            while(!orderPtr->isFullyMatched() && !orderQueue.empty()){
                OrderPtr oldestOrder = orderQueue.front();
                if (orderPtr->isMatchPossible(*oldestOrder)){
                    generateTrade(orderPtr, oldestOrder);
                }else {
                    throw std::runtime_error("control reached impossible state where orderPtr price matches the queue and quantity is not 0 yet the top of opposing queue does not match");
                }
                std::cerr << "\t 3: matching in deque loop:" << *topPriceOrders <<  std::endl;
                if (oldestOrder->isFullyMatched()){
                    orderQueue.pop_front();
                    orderIdOrdermap.erase(oldestOrder->orderId());
                    std::cerr << "\t 4: matching in deque loop:" << *topPriceOrders <<  std::endl;
                }
            }
            if ( orderQueue.empty()){
                auto pricekey = topPriceOrders->getPrice();
                priceQueueMap.erase(pricekey);
                priorityOrderQueue.pop();
            }
        } else break;
    }
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
#endif // __ORDERBOOK_H__