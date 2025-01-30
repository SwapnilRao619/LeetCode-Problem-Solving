## N
## Idea, approach and time complexity:
'''
The `Twitter` class simulates a simplified version of the Twitter platform, allowing users to post tweets, follow/unfollow other users, and retrieve the most recent 
tweets in their news feed. It uses two primary data structures: `defaultdict(set)` for managing follow relationships and `defaultdict(list)` for storing tweets with 
timestamps to maintain the order of tweets. The `postTweet` method records a tweet with a unique ID for a user and associates it with a timestamp. The `getNewsFeed` 
method retrieves the 10 most recent tweets from the user and their followees using a min-heap to efficiently manage and order the tweets by recency. This method 
includes the user's own tweets by default. The `follow` method allows a user to follow another user, adding the followee to the follower's set of followed users. The 
`unfollow` method removes a followee from the follower's set of followed users. The time complexity for `postTweet`, `follow`, and `unfollow` methods is O(1). The 
`getNewsFeed` method has a time complexity of O(n log k), where `n` is the number of users the current user follows (including themselves) and `k` is the number of 
tweets, due to heap operations.
'''

class Twitter:

    def __init__(self):
        self.fm=defaultdict(set)
        # Basically, we can also just do self.fm={} and then
        # in the other places, if followerId not in self.fm then 
        # self.fm[followerId]=set() and then, 
        # self.fm[followerId].add(followeeId)
        self.pm=defaultdict(list)
        self.gt=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.pm[userId].append([self.gt,tweetId])
        self.gt-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed=[]
        mh=[]
        self.fm[userId].add(userId)
        for fren in self.fm[userId]:
            if(fren in self.pm):
                li=len(self.pm[fren])-1
                gt,tid=self.pm[fren][li]
                mh.append([gt,tid,fren,li-1])
        heapq.heapify(mh)
        while mh and len(feed)<10:
            gt,tid,fren,li=heapq.heappop(mh)
            feed.append(tid)
            if(li>=0):
                gt,tid=self.pm[fren][li]
                heapq.heappush(mh,[gt,tid,fren,li-1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fm[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followeeId in self.fm[followerId]):
            self.fm[followerId].remove(followeeId)