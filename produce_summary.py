
print("Day 1")
daily_delivery_report = open("um-deliveries-20140519.txt")
for item in daily_delivery_report:
    item = item.rstrip()
    words = item.split('|')

    melon = words[0]
    count = words[1] 
    amount = words[2]

    print(f"Delivered {count} {melon}s for a total of ${amount}.")
daily_delivery_report.close()


print("Day 2")
daily_delivery_report = open("um-deliveries-20140520.txt")
for item in daily_delivery_report:
    item = item.rstrip()
    words = item.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for a total of ${amount}.")
daily_delivery_report.close()


print("Day 3")
daily_delivery_report = open("um-deliveries-20140521.txt")
for item in daily_delivery_report:
    item = item.rstrip()
    words = item.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for a total of ${amount}.")
daily_delivery_report.close()

