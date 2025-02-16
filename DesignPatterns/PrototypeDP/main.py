from DesignPatterns.PrototypeDP.zombiee import Zombiee

if __name__ == "__main__":
    z = Zombiee(100)
    arr = []
    for i in range(100):
        arr.append(z.clone())

    print(arr)