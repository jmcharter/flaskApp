class RetireApp:

    def __init__(self, income, homeowner, housecost,
                 bills, uage, rage, pension):
        self.income = income
        self.homeowner = homeowner
        self.housecost = housecost
        self.bills = bills
        self.uage = uage
        self.rage = rage
        self.pension = pension

    def Calculate(self):
        # Calculates amount of year until retirement
        self.ageDiff = self.rage - self.uage

        # User set life expectancy
        self.lifeEx = [75, 85, 95]

        # Calculates length of retirement
        self.retirement = [(self.lifeEx[0] - self.rage),
                           (self.lifeEx[1] - self.rage),
                           (self.lifeEx[2] - self.rage)]

        # Calculates the cost of bills from retirement to life expectancy
        self.lifeBills = [(self.retirement[0] *
                          (self.bills + self.housecost) * 12),
                          (self.retirement[1] *
                          (self.bills + self.housecost) * 12),
                          (self.retirement[2] *
                          (self.bills + self.housecost) * 12)]

        # Calculates money required by retirement age
        self.reqMoney = [(self.lifeBills[0] - self.pension),
                         (self.lifeBills[1] - self.pension),
                         (self.lifeBills[2] - self.pension)]

        # Calculates the amount of money users needs to save each month
        self.monthlySave = [((self.reqMoney[0] / self.ageDiff) / 12),
                            ((self.reqMoney[1] / self.ageDiff) / 12),
                            ((self.reqMoney[2] / self.ageDiff) / 12)]

        # Calculates the percenage of users income that needs to be saved
        self.incomePercent = [((self.monthlySave[0] / self.income) * 1200),
                              ((self.monthlySave[1] / self.income) * 1200),
                              ((self.monthlySave[2] / self.income) * 1200)]

    def Statement(self, currency, option=1):

        x = option

        statement = (
            """If you live until %i, then you'll need to save an additional:
%s%s

This means that as of now, and until retirement, you need to save:
%s%s per month
(That is %.2f%% of your annual salary) 
""" 
            % (self.lifeEx[x], currency, "{:,.2f}".format(self.reqMoney[x]),
                currency, "{:,.2f}".format(self.monthlySave[x]),
                self.incomePercent[x]))

        return statement

flask = RetireApp(16000, True, 0, 344444, 22, 65, 0)

option = 1
flask.Calculate()
print(flask.Statement("£"))
