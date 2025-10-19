import requests
import json
import time
from params import params, headers, card_features, deck_features



def extract_card_information(request_parameters, request_headers, card_attributes, deck):
    card_information = {}
    for card in deck["cards"]:
        time.sleep(1)
        request_parameters["exact"] = card
        response = requests.get(headers=request_headers, url="https://api.scryfall.com/cards/named", params=request_parameters)
        card_data = response.json()
        card_information[card] = {}
        for feature in card_attributes:
            try:
                card_information[card][feature] = card_data[feature]
            except: 
                None
    create_json(deck, card_information)


def create_json(deck, card_info):
    try:
        with open(f"{deck['name']}--deck.json", "w") as f:
            json.dump(card_info, f, indent=3)    
    except:
        print("Json Creating error")


    
if __name__ == "__main__":
    extract_card_information(params, headers, card_features, deck_features)
