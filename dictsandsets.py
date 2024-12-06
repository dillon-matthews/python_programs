import random
import json

def create_state_capital_file():
    state_capital_data = {
        "AL": {"state": "Alabama", "capital": "Montgomery"},
        "AK": {"state": "Alaska", "capital": "Juneau"},
        "AZ": {"state": "Arizona", "capital": "Phoenix"},
        "AR": {"state": "Arkansas", "capital": "Little Rock"},
        "CA": {"state": "California", "capital": "Sacramento"},
        "CO": {"state": "Colorado", "capital": "Denver"},
        "CT": {"state": "Connecticut", "capital": "Hartford"},
        "DE": {"state": "Delaware", "capital": "Dover"},
        "FL": {"state": "Florida", "capital": "Tallahassee"},
        "GA": {"state": "Georgia", "capital": "Atlanta"},
        "HI": {"state": "Hawaii", "capital": "Honolulu"},
        "ID": {"state": "Idaho", "capital": "Boise"},
        "IL": {"state": "Illinois", "capital": "Springfield"},
        "IN": {"state": "Indiana", "capital": "Indianapolis"},
        "IA": {"state": "Iowa", "capital": "Des Moines"},
        "KS": {"state": "Kansas", "capital": "Topeka"},
        "KY": {"state": "Kentucky", "capital": "Frankfort"},
        "LA": {"state": "Louisiana", "capital": "Baton Rouge"},
        "ME": {"state": "Maine", "capital": "Augusta"},
        "MD": {"state": "Maryland", "capital": "Annapolis"},
        "MA": {"state": "Massachusetts", "capital": "Boston"},
        "MI": {"state": "Michigan", "capital": "Lansing"},
        "MN": {"state": "Minnesota", "capital": "Saint Paul"},
        "MS": {"state": "Mississippi", "capital": "Jackson"},
        "MO": {"state": "Missouri", "capital": "Jefferson City"},
        "MT": {"state": "Montana", "capital": "Helena"},
        "NE": {"state": "Nebraska", "capital": "Lincoln"},
        "NV": {"state": "Nevada", "capital": "Carson City"},
        "NH": {"state": "New Hampshire", "capital": "Concord"},
        "NJ": {"state": "New Jersey", "capital": "Trenton"},
        "NM": {"state": "New Mexico", "capital": "Santa Fe"},
        "NY": {"state": "New York", "capital": "Albany"},
        "NC": {"state": "North Carolina", "capital": "Raleigh"},
        "ND": {"state": "North Dakota", "capital": "Bismarck"},
        "OH": {"state": "Ohio", "capital": "Columbus"},
        "OK": {"state": "Oklahoma", "capital": "Oklahoma City"},
        "OR": {"state": "Oregon", "capital": "Salem"},
        "PA": {"state": "Pennsylvania", "capital": "Harrisburg"},
        "RI": {"state": "Rhode Island", "capital": "Providence"},
        "SC": {"state": "South Carolina", "capital": "Columbia"},
        "SD": {"state": "South Dakota", "capital": "Pierre"},
        "TN": {"state": "Tennessee", "capital": "Nashville"},
        "TX": {"state": "Texas", "capital": "Austin"},
        "UT": {"state": "Utah", "capital": "Salt Lake City"},
        "VT": {"state": "Vermont", "capital": "Montpelier"},
        "VA": {"state": "Virginia", "capital": "Richmond"},
        "WA": {"state": "Washington", "capital": "Olympia"},
        "WV": {"state": "West Virginia", "capital": "Charleston"},
        "WI": {"state": "Wisconsin", "capital": "Madison"},
        "WY": {"state": "Wyoming", "capital": "Cheyenne"}
    }
    with open("state_capitals.json", "w") as file:
        json.dump(state_capital_data, file)

def load_state_capital_data():
    with open("state_capitals.json", "r") as file:
        return json.load(file)

def quiz_user(state_capital_dict):
    correct = 0
    incorrect = 0
    state_abbreviations = list(state_capital_dict.keys())
    random.shuffle(state_abbreviations)
    for state_abbr in state_abbreviations:
        state_name = state_capital_dict[state_abbr]["state"]
        capital = state_capital_dict[state_abbr]["capital"]
        user_answer = input(f"What is the capital of {state_name}? ").strip()
        if user_answer.lower() == capital.lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {capital}.")
            incorrect += 1
    print(f"\nQuiz Complete! Correct: {correct}, Incorrect: {incorrect}")

def main():
    create_state_capital_file()
    state_capital_dict = load_state_capital_data()
    quiz_user(state_capital_dict)

if __name__ == "__main__":
    main()
