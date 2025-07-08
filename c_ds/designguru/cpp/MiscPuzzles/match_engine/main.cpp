#include "order.h"
#include "orderBook.h"

#include "tradeHandler.h"

int main() {
    std::string line;
    TradeHandler tradeHandler;
    OrderBook orderBook(tradeHandler);
    InputProcessor inputProcessor(orderBook);
    while (getline(std::cin, line)){
        OrderPtr  orderPtr;
        try{
            inputProcessor.handleInput(line);
        } catch(std::exception const& excep){
            std::cerr << "Could not handle the order:" << line << " due to :" << excep.what() << std::endl;
            continue;
        }
    }
    return 0;
}