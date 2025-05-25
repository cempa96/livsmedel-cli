import sys
import requests
from tabulate import tabulate


url = "https://dataportal.livsmedelsverket.se/livsmedel/api/v1/livsmedel"
params = {
    "limit": 3000,
    "sprak": 1
}


def get_food_data() -> list: # (of tuples)
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        food_data = response.json()
        return [(item.get("nummer"), item.get("namn"), item.get("links")[0].get("href")) for item in food_data["livsmedel"]]
    
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching data: {e}")
        return []
    

def get_nutrients_data(food:tuple) -> list: # (of tuples)
    try:
        response = requests.get("https://dataportal.livsmedelsverket.se/livsmedel" + food[2])
        response.raise_for_status()
        nutrients_data = response.json()
        return [(nutrient.get("namn"), nutrient.get("varde"), nutrient.get("enhet")) for nutrient in nutrients_data]
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching nutrients data: {e}")
        return []
    

def print_nutrients_table(food:tuple, nutrients_list:list):
    table = [(nutrient, str(value) + unit) for nutrient, value, unit in nutrients_list]
    custom_order = (
        "Energi (kcal)", "Energi (kJ)",
        "Protein", "Kolhydrater, tillgängliga", "Fibrer", "Fett, totalt",
        "Summa mättade fettsyror", "Summa enkelomättade fettsyror", "Summa fleromättade fettsyror",
        "Vitamin A", "Retinol", "Betakaroten/β-Karoten", "Vitamin D", "Vitamin E", "Vitamin C",
        "Vitamin B6", "Vitamin B12", "Tiamin", "Riboflavin", "Folat, totalt",
        "Niacin", "Niacinekvivalenter",
        "Kolesterol", "Salt, NaCl", "Natrium, Na", "Kalium, K", "Kalcium, Ca", "Fosfor, P",
        "Järn, Fe", "Zink, Zn", "Selen, Se", "Jod, I",
        "DHA (C22:6)", "EPA (C20:5)", "DPA (C22:5)", "Arakidonsyra C20:4", "Arakidinsyra C20:0",
        "Linolensyra C18:3", "Linolsyra C18:2", "Oljesyra C18:1", "Stearinsyra C18:0", "Palmitoljesyra C16:1",
        "Palmitinsyra C16:0", "Myristinsyra C14:0", "Laurinsyra C12:0",
        "Avfall (skal etc.)", "Aska", "Alkohol", "Tillsatt socker", "Fritt socker",
        "Disackarider", "Monosackarider", "Sockerarter, totalt",
        "Fullkorn totalt"
    )
    table.sort(key=lambda x: custom_order.index(x[0]) if x[0] in custom_order else len(custom_order))
    
    print(f"\nNäringsinformation för {food[1]}")
    print(tabulate(table, headers=["Näringsämne", "Värde (per 100g)"], tablefmt="mixed_grid"))


def main():
    search_term = None
    if len(sys.argv) > 1:
        search_term = " ".join(sys.argv[1:]).strip()

    while True:
        if not search_term:
            search_term = input("\nAnge ett sökord för livsmedel: ").strip()
        print(f"\nSöker efter '{search_term}'...")
        
        food_data = get_food_data()
        if not food_data:
            print("\nKunde inte hämta livsmedelsdata.")
            search_term = None
            continue
        
        if not any(search_term.lower() in name[1].lower() for name in food_data):
            print(f"\nInga livsmedel hittades som innehåller '{search_term}'.")
            search_term = None
            continue
        
        i = 1
        matches = []
        for name in food_data:
            if search_term.lower() in name[1].lower():
                matches.append(name)
                print(f"{i}. {name[1]}")
                i += 1
        
        selection = tuple()
        while True:
            choice = input("\nVälj ett alternativ genom att ange motsvarande nummer: ")
            if not choice.isdigit() or not (1 <= int(choice) <= len(matches)):
                print("\nOgiltigt val. Försök igen.")
                continue
            selection = matches[int(choice) - 1]
            break
        
        nutrients_list = get_nutrients_data(selection)
        if not nutrients_list:
            print("\nKunde inte hämta näringsdata.")
            search_term = None
            continue

        print_nutrients_table(selection, nutrients_list)
        
        new_search = input("\nVill du göra en ny sökning? (ja/nej): ").strip().lower()
        if new_search in ["ja", "j"]:
            search_term = None
            continue
        
        print("\nAvslutar programmet.")
        return


if __name__ == "__main__":
    main()