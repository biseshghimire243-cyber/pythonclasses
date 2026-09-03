bill = float(input("Enter restaurant bill: "))
service_rate = float(input("Enter service charge percentage: "))

service_charge = bill * service_rate / 100
total = bill + service_charge

print("Original bill:", bill)
print("Service charge:", service_charge)
print("Total bill:", total)