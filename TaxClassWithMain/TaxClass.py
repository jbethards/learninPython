'''
Adding Taxes
'''


class taxCalculation:
    def __init__(self, TAX_AMOUNT, ITEM_COST):
        self.TAX_AMOUNT = TAX_AMOUNT
        self.ITEM_COST = ITEM_COST

    def getTax(self):
        return self.TAX_AMOUNT * self.ITEM_COST
