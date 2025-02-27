import time as t
import random
import numpy as np
import csv

header = ["Name", "Accuracy", "AvgTime", "Difficulty"]
leaderboard = "leaderboard.csv"

def saveresults(accuracy, avgtime, difficulty, header, leaderboard):
    try:
        rows = []
        with open(leaderboard, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) > 1:
            header = rows[0]
            data = rows[1:]
            best_time = min(float(row[2]) for row in data)

            if avgtime >= best_time:
                print("Your time was not faster. Leaderboard remains unchanged.")
                sort_leaderboard(leaderboard)
                return
        
        name = input("You set a new record! Enter your name: ")
        data.append([name, accuracy, avgtime, difficulty])
        data.sort(key=lambda x: float(x[2]))

        with open(leaderboard, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        
        print("Data ulozena uspesne.")
    except FileNotFoundError:
        print(f"Soubor '{leaderboard}' neexistuje")
    except Exception as e:
        print(f"Chyba: {e}")

def sort_leaderboard(leaderboard):
    try:
        with open(leaderboard, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) > 1:
            header = rows[0]
            data = rows[1:]
            data.sort(key=lambda x: float(x[2]))

            print("\nLeaderboard:")
            print(f"{'Jmeno':<20} {'Presnost':<10} {'Prumerny cas':<15} {'Obtiznost':<12}")
            for row in data:
                name, accuracy, avgtime, difficulty = row
                print(f"{name:<20} {accuracy:<10} {avgtime:<15} {difficulty:<12}")
        else:
            print("Leaderboard je prazdny")
        print("\n")
    except FileNotFoundError:
        print(f"Soubor '{leaderboard}' neexistuje")
    except Exception as e:
        print(f"Chyba: {e}")
def sort_leaderboard(leaderboard):
    try:
        with open(leaderboard, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) > 1:
            header = rows[0]
            data = rows[1:]
            data.sort(key=lambda x: float(x[2]))

            print("\nLeaderboard:")
            print(f"{'Jmeno':<20} {'Presnost':<10} {'Prumerny cas':<15} {'Obtiznost':<12}")
            for row in data:
                name, accuracy, avgtime, difficulty = row
                print(f"{name:<20} {accuracy:<10} {avgtime:<15} {difficulty:<12}")
        else:
            print("Leaderboard je prazdny")
        print("\n")
    except FileNotFoundError:
        print(f"Soubor '{leaderboard}' neexistuje")
    except Exception as e:
        print(f"Chyba: {e}")

print("Vitej v aritmeticke hre!")

while True:
    try:
        nums = []
        multnums = []
        multn = 0
        n = 0
        errors = 0
        limit = ""
        diff = input("Vyber obtiznost: [b]aby, [e]asy, [m]edium, [h]ard, e[x]treme, [c]ustom: ")
        if diff.lower() == "c":
            n = int(input("Jaka je maximalni hodnota, se kterou chces pocitat?: "))
            limit = input("Chces omezit nasobeni na malou nasobilku?: [a]no/[n]e: ")
        if diff.lower() == "b":
            n = 100
            limit = "a"
        if diff.lower() == "e":
            n = 1000
            multn = 15
        if diff.lower() == "m":
            n = 10000
            multn = 50
        if diff.lower() == "h":
            n = 100000
            multn = 100
        if diff.lower() == "x":
            n = 1000000
            multn = 200

        rounds = int(input("Kolik chces hrat kol?: "))
        if rounds <= 0 or n <= 0:
            raise ValueError
        if limit.lower() == "a":
            for i in range(1, 11):
                multnums.append(i)
        else:
            for i in range(multn):
                multnums.append(i+1)
        totaltime = 0
        for i in range(n):
            nums.append(i+1)
        print("Zacinas za 3...")
        t.sleep(1)
        print("Zacinas za 2...")
        t.sleep(1)
        print("Zacinas za 1...")
        t.sleep(1)
        for i in range(rounds):
            op = random.randint(1, 4)
            idx1 = random.randint(0, n-1)
            idx2 = random.randint(0, n-1)
            if op == 1:
                answered = False
                answer = nums[idx1] + nums[idx2]
                while not answered:
                    start = t.time()
                    usranswer = int(input(f"{nums[idx1]} + {nums[idx2]}: "))
                    if usranswer == answer:
                        print("Spravne!")
                        answered = True
                        end = t.time()
                        totaltime += end - start
                    else:
                        errors += 1
                        print("Spatne! Zkus to znovu.")
            elif op == 2:
                answered = False
                answer = nums[idx1] - nums[idx2]
                while not answered:
                    start = t.time()
                    usranswer = int(input(f"{nums[idx1]} - {nums[idx2]}: "))
                    if usranswer == answer:
                        print("Spravne!")
                        answered = True
                        end = t.time()
                        totaltime += end - start
                    else:
                        errors += 1
                        print("Spatne! Zkus to znovu.")
            elif op == 3:
                answered = False
                idx1 = random.randint(0, 9)
                idx2 = random.randint(0, 9)
                answer = multnums[idx1] * multnums[idx2]
                while not answered:
                    start = t.time()
                    usranswer = int(input(f"{nums[idx1]} * {nums[idx2]}: "))
                    if usranswer == answer:
                        print("Spravne!")
                        answered = True
                        end = t.time()
                        totaltime += end - start
                    else:
                        errors += 1
                        print("Spatne! Zkus to znovu.")
            elif op == 4:
                answered = False
                while nums[idx1] % nums[idx2] != 0:
                    idx1 = random.randint(0, n-1)
                    idx2 = random.randint(0, n-1)
                answer = nums[idx1] // nums[idx2]
                while not answered:
                    start = t.time()
                    usranswer = float(input(f"{nums[idx1]} / {nums[idx2]}: "))
                    if usranswer == answer:
                        print("Spravne!")
                        answered = True
                        end = t.time()
                        totaltime += end - start
                    else:
                        errors += 1
                        print("Spatne! Zkus to znovu.")
        attempts = rounds + errors
        avgtime = round(totaltime / rounds, 1)
        if errors > 0:
            accuracy = (rounds / (rounds + errors)) * 100
            accuracy = round(accuracy, 1)
        else:
            accuracy = 100
        print(f"Tvuj celkovy cas byl: {round(totaltime, 1)} sekund, prumerny cas na odpoved byl: {avgtime} sekund.")
        print(f"Udelal jsi {errors} chyb, tvoje presnost byla {accuracy} %")
        name = input("Zadej sve jmeno: ")
        saveresults(name, accuracy, avgtime, diff, header, leaderboard)
        sort_leaderboard(leaderboard)
        repeat = input("Chces hrat znovu? ([a]no/[n]e): ")

        if repeat.lower() == "a":
            continue
        else:
            print("\nUkoncuji program")
            t.sleep(1)
            break
    except ValueError:
        print("Zadal jsi neplatnou hodnotu")
        continue
    except KeyboardInterrupt:
        print("Ukoncuji program")
        t.sleep(1)
        break
    except Exception as e:
        print(e)
        continue
