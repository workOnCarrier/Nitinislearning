from collections import defaultdict
import heapq

class TwWrap:
    def __init__(self, twlist):
        self.twlist = twlist
        self.offset = -1
    def getLatest(self):
        if -self.offset > len(self.twlist):
            raise Exception(f"trying to access data beyond size {self.offset} : {self.twlist}")
        val = self.twlist[self.offset][1]
        return val
    def next(self):
        self.offset -= 1
    def hasMore(self):
        if -self.offset > len(self.twlist):
            return False
        return True
    def __lt__(self, other):
        return self.twlist[self.offset][0] <  other.twlist[other.offset][0] 
    def __repr__(self):
        string = f" offset: {self.offset} in : {self.twlist} \t"
        return string

class Twitter:
    def __init__(self):
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)
        self.seqNo = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.seqNo += 1
        twlist = self.tweetmap[userId].append([-self.seqNo, tweetId])

    def getNewsFeed(self, userId: int) -> list:
        result, pq = [], []
        followedList = [followed for followed in self.followmap[userId]]
        followedList.append(userId)
        for followed in followedList:
            if followed not in self.tweetmap:
                continue
            heapq.heappush(pq, TwWrap(self.tweetmap[followed]))
        for _ in range(10):
            if not pq:
                break
            twtop = heapq.heappop(pq)
            try:
                val = twtop.getLatest()
                twtop.next()
                result.append(val)
            except exc:
                print(f"\t {pq}")
            if twtop.hasMore():
                heapq.heappush(pq, twtop)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        if followerId not in self.followmap[followerId]:
            self.followmap[followerId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap:
            if followeeId in self.followmap[followerId]:
                self.followmap[followerId].remove(followerId)
        

def test_1():
    # ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]
    t = Twitter()
    t.postTweet(1, 10)
    t.postTweet(2, 20)
    print(t.getNewsFeed(1))
    print(t.getNewsFeed(2))
    t.follow(1,2)
    print(t.getNewsFeed(1))
    print(t.getNewsFeed(2))
    t.unfollow(1, 2)
    print(t.getNewsFeed(1))

def test_2():
    # ["Twitter", "postTweet", [1, 1], "postTweet", [1, 2], "postTweet", [1, 3], "postTweet", [1, 4], "postTweet", [1, 5], "postTweet", [2, 6], "postTweet", [2, 7], "follow", [1, 2], "getNewsFeed", [1], "unfollow", [1, 2], "follow", [1, 2], "getNewsFeed", [1], "postTweet", [2, 8], "getNewsFeed", [1], "unfollow", [1, 2], "getNewsFeed", [1]]
    t = Twitter()
    t.postTweet(1,1)
    t.postTweet(1,2)
    t.postTweet(1,3)
    t.postTweet(1,4)
    t.postTweet(1,5)
    t.postTweet(2,6)
    t.postTweet(2,7)
    t.follow(1,2)
    print(t.getNewsFeed(1))
    t.unfollow(1,2)
    t.follow(1,2)
    print(t.getNewsFeed(1))
    t.postTweet(2,8)
    print(t.getNewsFeed(1))
    t.unfollow(1,2)
    print(t.getNewsFeed(1))


if __name__ == "__main__":
    test_2()