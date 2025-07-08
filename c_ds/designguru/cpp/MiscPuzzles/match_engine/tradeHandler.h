#ifndef __TRADEHANDLER_H__
#define  __TRADEHANDLER_H__

class Trade{
public:
    Trade(OrderPtr aggressor, OrderPtr resting, int matchPrice, int matchQuantity): m_aggOrder(aggressor), m_restOrder(resting), m_matchPrice(matchPrice), m_matchQuantity(matchQuantity){}
    Trade(const Trade&) = delete;
    Trade& operator=(Trade & ) = delete;
    OrderPtr aggressor() {return m_aggOrder;}
    OrderPtr resting() {return m_restOrder;}
    int quantity() {return m_matchQuantity;}
private:
    OrderPtr    m_aggOrder;
    OrderPtr    m_restOrder;
    int         m_matchPrice;
    int         m_matchQuantity;
};
typedef std::shared_ptr<Trade> TradePtr;


class TradeHandler{
public:
    TradeHandler(){}
    void submitTrade(TradePtr trade);
};

#endif // __TRADEHANDLER_H__