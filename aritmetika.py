import time as t
import random
nums = []
multnums = []
mistakes = 0
print("Vitej v aritmeticke hre!")
while True:
    try:
        nums = []
        multnums = []
        mistakes = 0
        n = int(input("Jaka je maximalni hodnota, se kterou chces pocitat?: "))
        limit = input("Chces omezit nasobeni na malou nasobilku?: [a]no/[n]e: ")
        rounds = int(input("Kolik chces hrat kol?: "))
        if n <= 0 or rounds <= 0:
            print("Zadej kladne cislo!")
            continue
        print("Zacinas za 3...")
        t.sleep(1)
        print("Zacinas za 2...")
        t.sleep(1)
        print("Zacinas za 1...")
        t.sleep(1)
        if limit.lower() == "a":
            for i in range(11):
                multnums.append(i)
            multn = 9
        else:
            for i in range(n+1):
                multn = n
        print(multnums)
        totaltime = 0
        for i in range(n+1):
            nums.append(i)
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
                        print("Spatne! Zkus to znovu.")
                        mistakes += 1
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
                        print("Spatne! Zkus to znovu.")
                        mistakes += 1
            elif op == 3:
                answered = False
                idx1 = random.randint(0, multn-1)
                idx2 = random.randint(0, multn-1)
                answer = multnums[idx1] * multnums[idx2]
                while not answered:
                    start = t.time()
                    usranswer = int(input(f"{nums[idx1]}*{nums[idx2]}: "))
                    if usranswer == answer:
                        print("Spravne!")
                        answered = True
                        end = t.time()
                        totaltime += end - start
                    else:
                        print("Spatne! Zkus to znovu.")
                        mistakes += 1
            elif op == 4:
                answered = False
                while nums[idx1] % nums[idx2] != 0:
                    idx1 = random.randint(0, n-1)
                    idx2 = random.randint(0, n-1)
                answer = nums[idx1] // nums[idx2]
                while not answered:
                    start = t.time()
                    usranswer = float(input(f"{nums[idx1]}/{nums[idx2]}: "))
                    if usranswer == answer:
                        print("Spravne!")
                        answered = True
                        end = t.time()
                        totaltime += end - start
                    else:
                        print("Spatne! Zkus to znovu.")
                        mistakes += 1
        print(f"Tvuj celkovy cas byl: {round(totaltime, 1)} sekund, prumerny cas na odpoved byl: {round(totaltime/rounds, 1)} sekund.")
        print(f"Udelal jsi {mistakes} chyb. Tvoje presnost byla {round((rounds-mistakes)/rounds*100, 1)}%.")
        repeat = input("Chces hrat znovu? ([a]no/[n]e): ")
        if repeat.lower() == "a":
            continue
        else:
            print("Ukoncuji program")
            t.sleep(1)
            break
    except ValueError:
        print("Zadej platne cislo!")
        continue
    except KeyboardInterrupt:
        print("Ukoncuji program")
        t.sleep(1)
        break
    except Exception as e:
        print(e)
        continue