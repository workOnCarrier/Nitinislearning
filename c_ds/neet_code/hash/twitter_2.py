from collections import defaultdict
import heapq

class TwWrap:
    def __init__(self, twmap):
        self.twmap = twmap
        self.offset = -1
    def __lt__(self, other):
        # if not self.hasMore():
        #     return False
        # if not other.hasMore():
        #     return True
        return self.twmap[self.offset][0] < other.twmap[other.offset][0]
    def getVal(self):
        if -self.offset > len(self.twmap):
            raise Exception(f" requested offset: {self.offset} is invalid in {self.twmap}")
        return self.twmap[self.offset][1]
    def moveNext(self):
        self.offset -= 1
    def hasMore(self):
        return -self.offset <= len(self.twmap)
    def __repr__(self):
        string = f" offset: {self.offset} in : {self.twmap} \t"
        return string

class Twitter:
    def __init__(self):
        self.twmap = defaultdict(list)
        self.followmap = defaultdict(set)
        self.seqNo = 0
        self.fetchCount = 10
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.seqNo += 1
        self.twmap[userId].append((-self.seqNo, tweetId))

    def getNewsFeed(self, userId: int) -> list:
        result, pq = [], []
        following = [followee for followee in self.followmap[userId]]
        following.append(userId)
        for follow in following:
            if len(self.twmap[follow]) > 0:
                pq.append(TwWrap(self.twmap[follow]))
        heapq.heapify(pq)
        for _ in range(self.fetchCount):
            if not pq:
                break
            topts = heapq.heappop(pq)
            result.append(topts.getVal())
            topts.moveNext()
            if topts.hasMore():
                heapq.heappush(pq, topts)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap and followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)       

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

def test_3():
    # ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
    # [[],      [1,5],      [1],            [1,2],  [2,6],      [1],         [1,2],     [1]]
    t = Twitter()
    t.postTweet(1,5)
    print(t.getNewsFeed(1))
    t.follow(1, 2)
    t.postTweet(2,6)
    print(t.getNewsFeed(1))
    t.unfollow(1, 2)
    print(t.getNewsFeed(1))


if __name__ == "__main__":
    test_3()