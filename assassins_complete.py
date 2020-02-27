from random import shuffle
from random import randint
import csv

data = []

def add_assassin():
    name = raw_input("Assassin Name: ")
    data.append([name, "ALIVE", 0, 1])
    print(name + " added as ALIVE and with 1 Immunity")

def main():
    with open('assassins.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data.append(row)
        File.close()
    print(data)

    print("Welcome to the Assassins Admin Tool! What would you like to do?")
    while True:
        choice = input("Choose one:\n"
        "1. Add a new assassin\n"
        "2. Update an assassin's immunity count\n"
        "3. Report an assassination\n"
        "4. Revive an assassin\n"
        "5. Get new target pairings\n"
        "6. Output leaderboard\n"
        "7. Get a random assassin's name for revival\n"
        "8. Save Choices to CSV and Exit (DO THIS LAST BEFORE YOU LEAVE VERY IMPORTANT)\n"
        "Choice: ")

        if choice == 1:
            add_assassin()
        elif choice == 8:
            f = open('assassins.csv', 'w')
            with f:
                writer = csv.writer(f)
                writer.writerows(data)
            print("Actions Saved. Goodbye!")
            break
        else:
            print("Pick a valid option please!")

if __name__ == "__main__":
    main()
