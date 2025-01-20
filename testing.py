from page_statist import page_statistic_df
# import asyncio
# from latest_post import fetch_latest_9gag_post
# from post_statist import fetch_post_details

# get_post = asyncio.run(fetch_latest_9gag_post())
# post_details = asyncio.run(fetch_post_details(get_post[0]["url"]))


df = page_statistic_df()
print(df)
