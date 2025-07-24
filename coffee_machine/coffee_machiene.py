from menu import MENU
from resources import resources

penny, nickel, dime, quarter = 0.01, 0.05, 0.1, 0.25
money_inserted = 0
coffee_costs = 0
need = (0, 0, 0)
profit = 0

def show_report():
    """Resouces sözlüğü üzerinde işlem yapmamak için bir sözlük oluşturdum ek olarak düzenli olması için fonksiyon içinde oldu"""
    report = dict(resources)
    report["Money"] = money_inserted
    return True

def resource_sufficient(choice):
    """kaynak karşılaştırması yapıldı"""
    check_user = MENU[choice]
    coffee_need = check_user["ingredients"]["coffee"]
    water_need = check_user["ingredients"]["water"]
    milk_need = check_user["ingredients"].get("milk", 0)  
    
    if resources["coffee"] < coffee_need:
        print("Sorry, there is not enough coffee.")
        return False
    if resources["milk"] < milk_need:
        print("Sorry, there is not enough milk.")
        return False
    if resources["water"] < water_need:
        print("Sorry, there is not enough water.")
        return False
    return coffee_need , milk_need , water_need

def calculate_money():
    """para hesaplama işi burada dönüyor. penny nickel dime ve quarter hesaplaması yapıp değer döndürüyor"""
    check_penny = penny * int(input("How many pennies you have: "))
    check_nickel = nickel * int(input("How many nickels you have: "))
    check_dime = dime * int(input("How many dimes you have: "))
    check_quarter = quarter * int(input("How many quarters you have: "))
    total_money = check_penny + check_nickel + check_dime + check_quarter
    return total_money

def transaction(choice, money_inserted, need):
    """para iletimine bakıldı eğer iletim yapılacak kadar para varsa kaynaklardan düşüldü"""
    global profit
    cost = MENU[choice]["cost"]

    if money_inserted < cost:
        print(f"You inserted ${money_inserted} but the coffee price is ${cost}. Money refunded.")
        return False
    refund = round(money_inserted - cost, 2)
    if refund > 0:
        print(f"Here is ${refund} in change.")

    # Kaynaklardan düş
    resources["water"] -= need[1]
    resources["milk"] -= need[2]
    resources["coffee"] -= need[0]
    profit += cost

    print(f"Here is your {choice}. Enjoy!")
    return True

def make_coffee():
    """her şeyin döndüğü fonksiyon bu"""
    global money_inserted , coffee_costs , need
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower() 
    if choice == "off":
        print("Turning off...")
        return False
    if choice == "report":
        print(show_report())
    if choice not in MENU:
        print("Invalid Input")
        return True 
    need = resource_sufficient(choice)
    if not need:
        return True
    coffee_costs = MENU[choice]["cost"]
    money_inserted = calculate_money()
    print(f"You inserted ${money_inserted}, coffee costs ${coffee_costs}")

    transaction(choice, money_inserted, need)
    return True    

while True:
    if not make_coffee():
        break
