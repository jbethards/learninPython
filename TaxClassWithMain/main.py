from TaxClassWithMain import TaxClass


def main():
    taxes = TaxClass.taxCalculation(25, .5)
    print(taxes.getTax())
if __name__=="__main__":
    main()