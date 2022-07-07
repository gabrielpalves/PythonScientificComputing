import math

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        self.ledger.append({"amount": -amount, "description": description})
        if not self.check_funds():
            del self.ledger[-1]
            return False
        return True
    
    def get_balance(self):
        money = 0
        for i in self.ledger:
            money = money + i["amount"]
        return money

    def check_funds(self, amount=0):
        money = self.get_balance()
        if amount != 0:
            money = money - amount

        if money < 0: # not possible to withdraw
            return False
        else: # a withdraw took place
            return True
    
    def transfer(self, amount, cat):
        if self.get_balance()-amount >= 0:
            cat.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + cat.name)
            return True
        else:
            return False
    
    def __str__(self):
        n = 30-len(self.name) # number os asterisks
        title = ""
        for j in range(2):
            if j == 1:
                title = title + self.name
            for i in range(round(n/2)):
                title = title + "*"
        
        output = title + "\n"

        total = 0
        for i in self.ledger:
            amount = i["amount"]
            total = total + amount

            # adjust amount
            am = str(amount)
            dotpos = am.find(".")
            if dotpos == -1:
                am = am + ".00"
            elif dotpos+3 < len(am):
                am = am[:dotpos+2]
            elif dotpos+3 > len(am):
                for j in range(dotpos+3-len(am)):
                    am = am + "0"
            
            # adjust description
            desc = i["description"]
            if len(desc) > 23:
                desc = desc[0:23]
            else:
                for j in range(23-len(desc)):
                    desc = desc + " "
            
            for j in range(30-len(desc)-len(am)):
                desc = desc + " "
            output = output + desc + am + "\n"
        
        output = output + "Total: " + str(total)
        return output
        


def create_spend_chart(categories):
    chart = list()
    title = "Percentage spent by category"
    output = title + "\n"
    totalwithdraw = 0
    for i in categories:
        total = 0
        withdraw = 0
        deposit = 0
        for j in i.ledger:
            amount = j["amount"]
            if amount < 0:
                withdraw = withdraw + amount
            else:
                deposit = deposit + amount
            total = total + amount

        totalwithdraw = totalwithdraw + withdraw
        spentPercentage = int(math.floor(-withdraw*10/deposit)*10)

        #             0       1      2        3         4
        chart.append([i.name, total, deposit, withdraw, spentPercentage])
    
    for i in range(len(chart)):
        chart[i][4] = int(math.floor(chart[i][3]*10/totalwithdraw)*10)
    
    for j in range(100,-1,-10):
        text = ""
        if j != 100:
            if j == 0:
                text = text + "  "
            else:
                text = text + " "

        text = text + str(j) + "| "

        maxname = 0
        for i in chart:
            if i[4] >= j:
                text = text + "o  "
            else:
                text = text + "   "

            if len(i[0]) > maxname:
                maxname = len(i[0])
        output = output + text + "\n"

    # dashes
    output = output + "    "
    for i in range(len(text)-4):
        output = output + "-"
    output = output + "\n"

    for j in range(maxname):
        text = "     "
        for i in chart:
            name = i[0]
            if j <= len(name)-1:
                text = text + name[j] + "  "
            else:
                text = text + "   "
        output = output + text + "\n"
    output = output[:-1]
    return output