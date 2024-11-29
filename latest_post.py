import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def fetch_lastest_9gag_post():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://9gag.com")

        # Wait for content to load
        await page.wait_for_timeout(3000)  # Adjust as needed

        # Get the full page content after rendering
        content = await page.content()
        await browser.close()

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Find post data after JavaScript has rendered the page
        post_data = []
        soup = BeautifulSoup(content, 'html.parser')

        # Start by inspecting top-level elements
        body = soup.find('body')  # This will get the <body> tag
        list_container = body.find('div', class_='list-container')  # Find top-container, adjust if needed
        post_data = []

        if list_container:
            # Loop through posts or containers inside list-container
            for post in list_container.find_all('a', class_='badge-evt badge-track', limit=1):
                href = post.get('href')
                data_entry_id = post.get('data-entry-id')

                if href and data_entry_id:
                    full_url = "https://9gag.com" + href
                    post_data.append({'url': full_url, 'id': data_entry_id})

        # Print the results
        print("Top Post URL and ID:")
        for post in post_data:
            print(f"URL: {post['url']} | ID: {post['id']}")


# Run the async function
asyncio.run(fetch_lastest_9gag_post())
