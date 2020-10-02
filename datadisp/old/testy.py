from dataexploit import Datagrab
import random
def test():
    vanilla = Datagrab().vanilla_product()
    print(vanilla)

def random_number():
    y = random.sample(range(1, 100), 99)
    print(y)

def foring():
    inputer = input("Entrez l'input : ")
    ex = ["a", "b", "c", "d"]
    if inputer in ex:
        print("OK")
    else:
        print("not OK")

def blabla():
    #name = "X"
    name = "X"
    globals()[f"blabla{name}"] = 42
    print(blablaX)

    x = 0
    globals()[f"blabla{x}"] = 42
    print(blabla0)
blabla()