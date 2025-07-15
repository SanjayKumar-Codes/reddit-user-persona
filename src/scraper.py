import os
from typing import List, Tuple
import praw
from dotenv import load_dotenv

load_dotenv()

def init_reddit():
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    return reddit

def fetch_user_activity(reddit, username: str, limit: int = 100) -> Tuple[List[str], List[str]]:
    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=limit):
            posts.append(f"[POST] {submission.title}\n{submission.selftext}\n(Subreddit: {submission.subreddit})\n---")
        for comment in user.comments.new(limit=limit):
            comments.append(f"[COMMENT] {comment.body}\n(Subreddit: {comment.subreddit})\n---")
    except Exception as e:
        print(f"Error fetching data for {username}: {e}")

    return posts, comments
