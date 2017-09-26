def main():
    get_info()



def get_info():
    loans = ("Enter the amount your loans cost a month: ")
    gas = ("Enter the amount gas will cost you in a month: ")
    insurance = ("Enter how much insurance is per month: ")
    maintenance = ("Enter the amount you spend on maintance a month: ")
    annual_cost = (loans + gas + insurance + maintenance)
    return annual_cost


def greeting(cost):
    print("Your annual cost for your car will be "+ cost)

    main()
