# import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

from helpers.helpers import parse_count

async  def fetch_post_details(post_url):
    """
    Fetch the upvotes, downvotes, and comments of a 9GAG post.

    Args:
        post_url (str): URL of the 9GAG post.

    Returns:
        dict: A dictionary containing the upvotes, downvotes, and comments.
    """
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        page = await browser.new_page()
        await page.goto(post_url)

        # Wait for content to load
        await page.wait_for_timeout(3000)  # Adjust as needed

        # Get the full page content after rendering
        content = await page.content()
        await browser.close()

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Scrape upvotes, downvotes, and comments
        details = {"upvotes": 0, "downvotes": 0, "comments": 0}

        upvote_element = soup.find('span', class_='upvote')
        downvote_element = soup.find('span', class_='downvote')
        comment_element = soup.find('span', class_='post-tab-bar__count')
        if upvote_element:
            details["upvotes"] = parse_count(upvote_element.text)
        if downvote_element:
            details["downvotes"] = parse_count(downvote_element.text)
        if comment_element:
            details["comments"] = parse_count(comment_element.text)

        print(details)
        return details

# Test the function
#if __name__ == "__main__":
 #   post_url = "https://9gag.com/gag/aZZ0dG9"
  #  post_details = asyncio.run(fetch_post_details(post_url))
   # print(post_details)
