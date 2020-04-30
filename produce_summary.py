
def produce_summary_report(report_location):
    print(report_location[12:20])
    delivery_report = open(report_location)
    for item in delivery_report:
        item = item.rstrip()
        relevant_report_values = item.split('|')

        melon = relevant_report_values[0]
        count = relevant_report_values[1] 
        price = relevant_report_values[2]

    print(f"Delivered {count} {melon}s for a total of ${price}.")
    delivery_report.close()


print("Day1")
produce_summary_report("um-deliveries-20140519.txt")
print("Day2")
produce_summary_report("um-deliveries-20140520.txt")
print("Day3")
produce_summary_report("um-deliveries-20140521.txt")
