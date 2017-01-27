bill_amount = raw_input("What is the bill amount?")
bill_amount = float(bill_amount)
tip = raw_input("What is the tip percentage?")
tip = float(tip)
people = raw_input("How many people in the group?")
people = int(people)

def calculate_tip(bill, tip_percent):
    percent = tip_percent/100.0
    total_tip = bill*percent
    return total_tip

def calculate_amount(bill, tip_amount):
    return_bill = bill + tip_amount
    return return_bill

def split_bill(bill_total, num_people):
    return_bill = bill_total/num_people
    return return_bill


tip_result = calculate_tip(bill_amount, tip)
amount_total = calculate_amount (bill_amount, tip_result)
split_amount = split_bill(amount_total, people)
print "The tip is", tip_result
print "The total amount is", amount_total
print "The split amount is", split_amount


