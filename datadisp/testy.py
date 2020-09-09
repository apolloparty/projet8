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

foring()