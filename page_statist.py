import json
import pandas as pd
import cloudscraper


def page_statistic_df():
    # Create a CloudScraper instance
    scraper = cloudscraper.create_scraper()
    url_9gag = "https://9gag.com/v1/feed-posts/type/home"
    response = scraper.get(url=url_9gag)
    response_json = json.loads(response.text)

    keys_to_keep = ['id', 'title', 'description', 'type', 'nsfw', 'upVoteCount', 'downVoteCount' ]
    all_filtered_data = []
    for data_per_post in response_json["data"]["posts"]:
        filtered_data = {key: data_per_post[key] for key in keys_to_keep}
        all_filtered_data.append(filtered_data)

    # Convert to a DataFrame
    df = pd.DataFrame(all_filtered_data)
    return df