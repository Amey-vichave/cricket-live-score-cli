from requests import get
from pprint import PrettyPrinter

printer = PrettyPrinter()

URL = 'https://api.cricapi.com'
API_KEY = '87b6511f-8cc0-4995-9d7e-52769e1b95b4'

def get_data():
    endpoint = f"/v1/currentMatches?apikey={API_KEY}&ofsfset=0"
    url = URL + endpoint
    data = get(url).json()
    return data

def show_match():
    data = get_data()
    matches = data.get("data", [])
    for i, match in enumerate(matches, start=1):
        name = match.get("name")
        print("-----------------------------------")
        print(f'({i}).{name}')
    
    
    while True:
        select_match = input("Enter Match number to view score! ")
        if select_match.isdigit():
            index = int(select_match)
            if 0 <= index <= len(matches):
                selected = matches[index - 1]
                print("\nyou selected:")
                print(f'Match {index}: {selected.get('name')}')
                return selected
            else:
                print("Enter valid match number.")
                continue
        else:
            print("Please enter a number.")
            continue

       
def match_details():
    match = show_match()
    print("------------------------------")
    print("Match details:")
    date = match.get("date")
    venue = match.get("venue")
    teams = match.get("teams")
    score = match.get("score")
    print(" vs ".join(teams) if teams else "N/A")
    print("Venue: ",venue)
    print("Date: ",date)
    if score:
        print("\nScore:")
        for inning in score:
            inning_name = inning.get("inning","Unknown inning")
            run = inning.get("r", "-")
            over = inning.get("o", "-")
            wicket = inning.get("w", "-")
            print(f'{inning_name}: {run}/{wicket} in {over} Overs')
        print("------------------------------")
    else:
        print("Score not found.")
        print("------------------------------")
    


        



            
            
            
        

match_details()

