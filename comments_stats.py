import cloudscraper
import pandas as pd


def fetch_comments(post_id, count=10, sort_type="hot", next_token=None):
    """
    Fetch comments from a 9GAG post using the observed API.
    
    :param post_id: The ID of the 9GAG post
    :param count: Number of comments to fetch per request (default 10).
    :param sort_type: Sorting type ('hot', 'fresh', etc.).
    :param next_token: Token for pagination (default None).
    :return: List of comments with relevant information.
    """
    scraper = cloudscraper.create_scraper()
    base_url = "https://comment-cdn.9gag.com/v2/cacheable/comment-list.json"
    params = {
        "appId": "a_dd8f2b7d304a10edaf6f29517ea0ca4100a43d1b",
        "count": count,
        "type": sort_type,
        "url": f"http://9gag.com/gag/{post_id}",
        "origin": "https://9gag.com",
    }
    if next_token:
        params["next"] = next_token

    # Make the request
    response = scraper.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        payload = data.get("payload", [])
        comments = payload.get("comments", [])
        next_token = payload.get("next")
        print(data)
        # Extract relevant data
        comment_list = [
            {
                "comment_id": comment.get("commentId"),
                "text": comment.get("text"),
                "timestamp": comment.get("timestamp"),
            }
            for comment in comments if comment.get('type') == 'text'
        ]
        df = pd.DataFrame(comment_list)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        return df, next_token
    else:
        print(f"Error {response.status_code}: {response.text}")
        return [], None

