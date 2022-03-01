from click import password_option
from instaloader import Instaloader, Profile
from secrets import secrets
from datetime import datetime
from itertools import dropwhile, takewhile


username = secrets.get('USERNAME')
password = secrets.get('PASSWORD')

START = datetime(2021, 12, 24)
END = datetime(2022, 2, 24)

def start_ig_engagement(username, password):
    """
    Start the engagement with the given username and password.
    """
    # Create an Instaloader instance.
    loader = Instaloader()

    # Login to Instagram.
    loader.login(username, password)

    return loader

def get_stats(loader, target_profile):
    """
    Get the stats for the target profile.
    """
    profile = Profile.from_username(loader.context, target_profile)
    posts = profile.get_posts()
    
    num_followers = profile.followers
    total_num_likes = 0
    total_num_comments = 0
    total_num_posts = 0
    post_dates = []
    
    for post in posts:
        if post.date > START:
            total_num_likes += post.likes
            total_num_comments += post.comments
            total_num_posts += 1
            post_dates.append(post.date)
        
    return num_followers, total_num_likes, total_num_comments, total_num_posts, post_dates

    
    
def cal_engagement(num_followers, total_num_likes, total_num_comments, total_num_posts):
    engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
    pct_engagement = engagement * 100
    print(f"IG Engagement: {pct_engagement:.2f}%")


if __name__ == "__main__":
    target_profile = input("Enter IG handle: ")
    loader = start_ig_engagement(username, password)
    num_followers, total_num_likes, total_num_comments, total_num_posts, post_dates = get_stats(loader, target_profile)
    cal_engagement(num_followers, total_num_likes, total_num_comments, total_num_posts)
    print(f"Total Followers: {num_followers}")
    print(f"Total Posts: {total_num_posts}")
    print(f"Total Likes: {total_num_likes}")
    print(f"Total Comments: {total_num_comments}")