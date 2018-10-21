print("Usage: number {currency (US or E)} (enter 'done' to quit)")
print("Example: 100 US")

while True:
    input_str = raw_input("Enter: ")
    if input_str.lower() == "done":
        break
    try:
        input_list = input_str.split(" ")
        if len(input_list) == 0:
            print("invalid input")
        elif len(input_list) == 1:
            amount = float(input_list[0])
            euros = 0.7 * amount
            print("Since you didn't specify a currency, I'm assuming US to Euros.")
            print("{0} US dollars is equivalent to {1} Euros".format(amount, euros))
        elif len(input_list) == 2:
            amount = float(input_list[0])
            if input_list[1].upper() == 'US':
                euros = 0.7 * amount
                print("{0} US dollars is equivalent to {1:.4f} Euros".format(amount, euros))
            elif input_list[1].upper() == 'E':
                dollars = (10.0 / 7) * amount
                print('{0} Euros is equivalent to {1:.4f} US Dollars'.format(amount, dollars))
            else:
                print("invalid currency")
        else:
            print("invalid input")
    except:
        print("Usage: number {currency (US or E)} (enter 'done' to quit)")



