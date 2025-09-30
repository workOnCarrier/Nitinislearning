from collections import defaultdict, deque
import heapq
import itertools

class BankingSystem:
    def __init__(self):
        self.accounts = {}  # accountId -> current balance
        self.transactions = []  # (timestamp, type, details)
        self.transfer_counts = defaultdict(int)  # accountId -> number of transfers initiated
        self.scheduled_payments = defaultdict(dict)  # accountId -> {paymentId: (execTime, amount)}
        self.payment_counter = itertools.count(1)  # unique payment IDs
        self.history = defaultdict(list)  # accountId -> [(timestamp, balance)]
        self.spend_tracker = defaultdict(int)  # accountId -> total sent via transfers

    # ---------------- Core Requirements ---------------- #

    def CreateAccount(self, timestamp, accountId):
        if accountId not in self.accounts:
            self.accounts[accountId] = 0
            self.history[accountId].append((timestamp, 0))
            self.transactions.append((timestamp, "CreateAccount", accountId))

    def Deposit(self, timestamp, accountId, amount):
        if accountId in self.accounts:
            self.accounts[accountId] += amount
            self.history[accountId].append((timestamp, self.accounts[accountId]))
            self.transactions.append((timestamp, "Deposit", accountId, amount))

    def Transfer(self, timestamp, fromAccountId, toAccountId, amount):
        if fromAccountId not in self.accounts or toAccountId not in self.accounts:
            return None
        if self.accounts[fromAccountId] < amount:
            return None

        # Deduct and add
        self.accounts[fromAccountId] -= amount
        self.accounts[toAccountId] += amount

        # Track balances over time
        self.history[fromAccountId].append((timestamp, self.accounts[fromAccountId]))
        self.history[toAccountId].append((timestamp, self.accounts[toAccountId]))

        # Update transfer counts
        self.transfer_counts[fromAccountId] += 1
        transfer_label = f"Transfer{self.transfer_counts[fromAccountId]}"

        # Track total spending
        self.spend_tracker[fromAccountId] += amount

        self.transactions.append((timestamp, "Transfer", fromAccountId, toAccountId, amount, transfer_label))
        return transfer_label

    # ---------------- Follow-up Requirements ---------------- #

    def TopSpenders(self, timestamp, n):
        # Sort by total sent, break ties by accountId
        top = sorted(self.spend_tracker.items(), key=lambda x: (-x[1], x[0]))
        return [f"{acct}({amt})" for acct, amt in top[:n]]

    def SchedulePayment(self, timestamp, accountId, amount, delay):
        if accountId not in self.accounts or self.accounts[accountId] < amount:
            return None
        paymentId = next(self.payment_counter)
        execTime = timestamp + delay
        self.scheduled_payments[accountId][paymentId] = (execTime, amount)
        self.transactions.append((timestamp, "SchedulePayment", accountId, amount, delay, paymentId))
        return paymentId

    def CancelPayment(self, timestamp, accountId, paymentId):
        if accountId in self.scheduled_payments and paymentId in self.scheduled_payments[accountId]:
            del self.scheduled_payments[accountId][paymentId]
            self.transactions.append((timestamp, "CancelPayment", accountId, paymentId))

    def ProcessScheduled(self, timestamp):
        """Process all payments due up to this timestamp"""
        for acct, payments in list(self.scheduled_payments.items()):
            for pid, (execTime, amount) in list(payments.items()):
                if execTime <= timestamp:
                    if self.accounts[acct] >= amount:
                        self.accounts[acct] -= amount
                        self.history[acct].append((timestamp, self.accounts[acct]))
                        self.transactions.append((timestamp, "ScheduledDebit", acct, amount, pid))
                    del self.scheduled_payments[acct][pid]

    def GetBalance(self, timestamp, accountId, timeAt):
        if accountId not in self.accounts:
            return None
        # Binary search historical balances
        hist = self.history[accountId]
        lo, hi = 0, len(hist) - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if hist[mid][0] <= timeAt:
                ans = hist[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    def MergeAccount(self, timestamp, accountId1, accountId2):
        if accountId1 not in self.accounts or accountId2 not in self.accounts:
            return
        # Merge balances
        self.accounts[accountId1] += self.accounts[accountId2]
        self.history[accountId1].append((timestamp, self.accounts[accountId1]))
        # Merge spending history
        self.spend_tracker[accountId1] += self.spend_tracker[accountId2]
        # Merge transactions
        self.history[accountId1].extend(self.history[accountId2])
        self.history[accountId1].sort()
        # Remove accountId2
        del self.accounts[accountId2]
        del self.history[accountId2]
        self.transactions.append((timestamp, "MergeAccount", accountId1, accountId2))

# ---------------- Example Run ---------------- #
def run_commands(commands):
    bank = BankingSystem()
    results = []

    for cmd in commands:
        method = cmd[0]
        args = cmd[1:]
        func = getattr(bank, method)
        out = func(*args)

        # Only append results if the function returns something non-None
        if out is not None:
            results.append(out)

        # Special case: always process scheduled payments after each command
        if method != "ProcessScheduled":
            bank.ProcessScheduled(args[0])  # pass timestamp

    return results


# ---------------- Example Run ---------------- #
if __name__ == "__main__":
    commands = [
        ("CreateAccount", 1, "A1"),
        ("CreateAccount", 2, "A2"),
        ("Deposit", 3, "A1", 500),
        ("Deposit", 4, "A2", 200),
        ("Transfer", 5, "A1", "A2", 150),  # Expect "Transfer1"
        ("Transfer", 6, "A1", "A2", 50),   # Expect "Transfer2"
        ("TopSpenders", 7, 2),             # Expect ["A1(200)"]
        ("SchedulePayment", 8, "A1", 100, 5),  # payment scheduled for t=13
        ("GetBalance", 9, "A1", 12),       # balance before scheduled debit
        ("GetBalance", 14, "A1", 14),      # after scheduled debit processed
        ("MergeAccount", 15, "A1", "A2"),
        ("GetBalance", 16, "A1", 16),
    ]

    results = run_commands(commands)
    print("Outputs:")
    for r in results:
        print(r)
