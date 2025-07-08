#include "tradeHandler.h"


void TradeHandler::submitTrade(TradePtr trade){
    std::cout << "TRADE " << trade->resting()->orderId() << " " <<  trade->resting()->price() << " "  ;
     std::cout << trade->quantity()  << " " <<  trade->aggressor()->orderId() << " " ;
     std::cout << trade->aggressor()->price() << " " <<  trade->quantity() << std::endl;
}
