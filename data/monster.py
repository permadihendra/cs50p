import random

import requests


def get_monster():
    try:
        monster_name = ["acolyte", "griffon", "kobold"]
        monster_selected = random.choice(monster_name)
        url = f"https://www.dnd5eapi.co/api/2014/monsters/{monster_selected}"
        payload = {}
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return None
    except Exception as e:
        print("Error getting data: ", e)
        return None
