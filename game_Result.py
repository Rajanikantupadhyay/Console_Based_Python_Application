import requests
import validations

def find_game_deals():
    title = input("Enter the game title to search: ")

    url = f"https://www.cheapshark.com/api/1.0/deals?title={title}&limit=20"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            deals = data
        else:
            deals = data.get('deals', [])

        deals_to_show = deals[:5]

        if deals_to_show:
            print(f"\n=== Deals for {title} ===")
            for deal in deals_to_show:
                print(f"Title: {deal['title']}")
                print(f"Store: {deal['storeID']}")
                print(f"Normal Price: ${deal['normalPrice']}")
                print(f"Sale Price: ${deal['salePrice']}")
                print(f"Savings: {deal['savings']}%")
                print(f"Deal Rating: {deal['dealRating']}")
                store_link = deal.get('storeLink', 'No link available')
                print(f"Link: {store_link}\n")
        else:
            print(f"No deals found for {title}.")
    else:
        print("Error fetching data from API.")
