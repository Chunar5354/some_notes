## 355. Design Twitter

[Problem link](https://leetcode.com/problems/design-twitter/)

- My approach

I use two dictionaries to store the relationship of following and tweet posting. And use one list so save the tweets in their posting order.

```python
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.usersFollow = {}
        self.usersTweet = {}
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId in self.usersFollow:
            if userId in self.usersTweet:
                self.usersTweet[userId].add(tweetId)
            else:
                self.usersTweet[userId] = {tweetId}
        else:
            self.usersFollow[userId] = {userId}
            self.usersTweet[userId] = {tweetId}
        self.tweets = [tweetId] + self.tweets
            
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        for t in self.tweets:
            # Firstly search from current user
            if userId in self.usersTweet and t in self.usersTweet[userId]:
                res.append(t)
                if len(res) == 10:
                    return res
            else:
                # Then search from his followees
                if userId in self.usersFollow:
                    for user in self.usersFollow[userId]:
                        if t in self.usersTweet[user]:
                            res.append(t)
                            if len(res) == 10:
                                return res
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.usersFollow:
            self.usersFollow[followerId].add(followeeId)
        else:
            self.usersFollow[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.usersFollow and followeeId in self.usersFollow[followerId]:
            self.usersFollow[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```
