#inputs
##rent , foood , electricuty unit  , charge per unit , persons living in room/flat


##output
#total amount you have to pay



rent=int(input("Enter you hostel / flat rent = "))
food=int(input("Enter amount of food order= "))
electricity_spend=int(input("Enter the total of Electricity spend= "))
charge_per_unit=int(input("Enter charge per unit= "))
persons=int(input("Enter the number of persons living in room / flat= "))

total_bill=electricity_spend*charge_per_unit

output = (food + rent+ total_bill) // persons

print(f"Each person will pay = {output}")
