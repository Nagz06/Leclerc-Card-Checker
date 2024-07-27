import requests
import logging

ELECLERC_USERAGENT = "; ZeroProspectus/"
ELECLERC_API_KEY2 = "e7ccb7d3d2414eb2af4163fc91eb2793"
ELECLERC_USER_AGENT = f"{requests.utils.default_user_agent()}{ELECLERC_USERAGENT}93"

BASE_URL = "https://ws-eleclerc.easyworldcom.com/webservices/SoldeCarteV2.php"
PARAMS = {
    "env": "prod",
    "card": "2951999554167",
    "pin": "0609"
}

HEADERS = {
    "User-Agent": ELECLERC_USER_AGENT,
    "x-leclerc-api-key": ELECLERC_API_KEY2
}

def fetch_card_balance():
    try:
        response = requests.get(BASE_URL, params=PARAMS, headers=HEADERS)

        response.raise_for_status()

        card_balance = response.json()
        print("Card Balance Response:", card_balance)
    
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"Other error occurred: {err}")

if __name__ == "__main__":
    fetch_card_balance()
