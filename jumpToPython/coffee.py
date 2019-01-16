coffee = 10
while True:
    money = int(input("money input"))
    if money == 300:
        print("give coffee")
        coffee = coffee - 1
    elif money > 300:
        print("gice %d change" % (money-300))
        coffee = coffee - 1
    else:
        print("give money back, no coffee")
        print("rest cofee %d" % coffee)

    if not  coffee:
        print("sold out")
        break





