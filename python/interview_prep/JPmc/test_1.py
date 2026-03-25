'''
 Portfolio rebalancer
-- multiple assets
-- value of assets -- we would want to buy some and sell some
'''

'''
apple -- 100 shares at 150 $
msoft -- 50 at 400 
google -- 10 at 2800
-- rebalance -- target
apple -- 40%
msoft -- 35%
google -- 25%
--- constraint
rebalance only if deviation is > 5%
------
if apple less than 35% or greater than 45 % -- rebalance
ms                  < 30% or > 40 -- rebalance
google              < 20 % or > 30 % rebalance

e.g. google 19%, apple 45% , ms 36% --- total balance may vary --
-- print the change -- some orders --- to buy or sell
-- value of each component of the portfolio (after the change) 
-- final value 
'''
from collections import deque

class PortfolioBalancer:
    def __init__(self, portfolio: dict, weights: dict, variance: float) -> None:
        self.orig_port = portfolio
        self.curr_port = portfolio
        self.weights = weights
        self.variance = variance
        self.proportion = {}
        self.total_val = 0
        self.order_que = {}

    def IsBalanced(self) -> bool:
        # check if portfolio is balanced
        balanced = True
        for asset, val in self.curr_port.items():
            value, price = val[0], val[1]
            asset_val = value * price
            self.proportion[asset] = asset_val
            self.total_value += asset_val
        # get ratio of proportion
        for asset, val in self.proportion.items():
            self.proportion[asset] = val / self.total_value
            if self.proportion[asset] < (self.weights[asset] - self.variance) or self.proportion[asset] > (self.weights[asset] + self.variance):
                balanced = False
        print(f" total val: {self.total_value}  -- potfolio: {self.proportion}")
        print(f"portfolio balance check: {balanced}")
        return balanced

    def generate_balancing_orders(self) :
        # generate balanceing orders
        # while not IsBalanced()
        # how much to buy/sell 
        # -- buy_gap = (weights - variance) - curr_proportion of the asset 
        # -- sell_gap = (weights + variance) - curr_proportion of the asset 
        # buy_val = buy_gap * total_val 
        # numb of shares to buy --> (buy_val // price)  + 1
        #  sell_val = sell_gap * total_val
        # numb of share to seel --> (sel_val // price) + 1
        # generate report
        pass


def test():
    # asset: (value, price)
    portfolio = {'apple': (100, 150), 'msoft': (50, 400), 'google': (10, 2800)}
    weights = {'apple': 0.40, 'msoft': 0.35, 'google': 0.25}
    variance = 0.05
    pb = PortfolioBalancer(portfolio, weights, variance)
    if not pb.IsBalanced():
        pb.generate_balancing_orders()


if __name__ == "__main__":
    test()



