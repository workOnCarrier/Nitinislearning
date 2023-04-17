#include <iostream>
#include <cmath>
#include <queue>
#include <vector>
#include <stack>
#include <chrono>
#include <memory>


struct Order{
    std::string m_orderId;
    double m_price;
    double m_quantity;
    Order(std::string orderId, double price, double quantity):m_orderId(orderId), m_price(price), m_quantity(quantity){}
    // std::chrono::time_point<std::chrono::high_resolution_clock> m_orderTime;
} ;
template<typename Stream>
Stream& operator<< (Stream& stream, Order& order){
    stream << "\t" << order.m_orderId << " " << order.m_price << " " << order.m_quantity ;
    return stream;
}
typedef std::shared_ptr<Order> OrderPtr;
class SamePriceOrders{
    public:
    SamePriceOrders(OrderPtr &order):m_price(order->m_price), m_orderStack(){ m_orderStack.push(order);}
    double getPrice()const {return m_price;}
    private:
    double m_price;
    std::stack<OrderPtr> m_orderStack;

};
template<int N>
class OrderCompareAsc{
public:
    bool operator()(const Order &left, const Order & right){
        auto multiplier = pow(10, N);
        if (std::round(left.m_price * multiplier) <= std::round(right.m_price * multiplier)) return true;
        else return false;
    }
};
template<int N>
class OrderCompareDesc{
public:
    bool operator()(const Order &left, const Order & right){
        auto multiplier = pow(10, N);
        if (std::round(left.m_price * multiplier) >= std::round(right.m_price * multiplier)) return true;
        else return false;
    }
};
// typedef std::priority_queue<SamePriceOrders, std::vector<SamePriceOrders>, OrderCompare<4>> BuyOrderQueue;
// typedef std::priority_queue<SamePriceOrders, std::vector<SamePriceOrders>, OrderCompare<4, false>> SellOrderQueue;
typedef std::priority_queue<Order, std::vector<Order>, OrderCompareAsc<4>> BuyOrderQueue;
typedef std::priority_queue<Order, std::vector<Order>, OrderCompareAsc<4>> SellOrderQueue;

class OrderBook{
public:
    OrderBook(){
        m_buyQueue = BuyOrderQueue((OrderCompareAsc<4>()));
        m_sellQueue = SellOrderQueue(OrderCompareAsc<4>());
    }
    BuyOrderQueue m_buyQueue;
    SellOrderQueue m_sellQueue;
};
template <typename Stream>
Stream& operator << (Stream& stream, OrderBook& obj){
    stream << "==== sell order book ====" << std::endl;
    while(!obj.m_sellQueue.empty()){
        auto leastExpensive = obj.m_sellQueue.top();
        stream << leastExpensive << std::endl;
        obj.m_sellQueue.pop();
    }   
    stream << "==== buy order book ====" << std::endl;
    while (!obj.m_buyQueue.empty()){
        auto cheapestOrder = obj.m_buyQueue.top();
        stream << cheapestOrder << std::endl;
        obj.m_buyQueue.pop();
    }

    return stream;
}


void playOrderBook(){
    OrderBook obObj;
    obObj.m_buyQueue.push(Order(std::string("abc"), 20.0, 5.0));
    obObj.m_buyQueue.push(Order(std::string("xyz"), 22.0, 1.0));
    obObj.m_buyQueue.push(Order(std::string("zyz"), 19.0, 3.0));
    obObj.m_sellQueue.push(Order({"ghi", 30, 20}));
    obObj.m_sellQueue.push(Order({"ijk", 25, 20}));
    obObj.m_sellQueue.push(Order({"qnp", 27, 20}));
    obObj.m_sellQueue.push(Order({"nst", 35, 20}));
    std::cout << obObj << std::endl;;
}


int main(){
    playOrderBook();

    std::cout << "Hello world --- end of program" << std::endl;

    return 0;
}