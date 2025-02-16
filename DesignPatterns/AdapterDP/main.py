from DesignPatterns.AdapterDP.adapters.iciciBankAdapter import IciciBankAdapter
from DesignPatterns.AdapterDP.adapters.yesBankAdapter import YesBankAdapter
from DesignPatterns.AdapterDP.phonepe import Payment

if __name__ == "__main__":
    b1 = YesBankAdapter()
    b2 = IciciBankAdapter()
    p1 = Payment(b1)
    p2 = Payment(b2)

    print(p1.checkBalance())
    print(p2.checkBalance())