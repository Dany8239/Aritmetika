import time as t
import random
nums = []
multnums = []
print("Vitej v aritmeticke hre!")
while True:
    try:
        nums = []
        multnums = []
        n = int(input("Jaka je maximalni hodnota, se kterou chces pocitat?: "))
        limit = input("Chces omezit nasobeni na malou nasobilku?: [a]no/[n]e: ")
        rounds = int(input("Kolik chces hrat kol?: "))
        if limit.lower() == "a":
            for i in range(1, 11):
                multnums.append(i)
            multn = 9
        print(multnums)
        totaltime = 0
        for i in range(n):
            nums.append(i+1)
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
        print(f"Tvuj celkovy cas byl: {round(totaltime, 1)} sekund, prumerny cas na odpoved byl: {round(totaltime/rounds, 1)} sekund.")
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