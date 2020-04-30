
def produce_summary_report(report_date):
    """Funcion generates produce sumary reports for dates in dates_of_interest"""
    print("Date: " + report_date)
    """Outputs the dates for reports just above each report """
    delivery_report = open("um-deliveries-" + report_date + ".txt")
    """sets variable to the um-delivery reports """
    for item in delivery_report:
        """Iterates through deivery_report"""
        item = item.rstrip()
        """removes trailing characters from items in delivery reports"""
        relevant_report_values = item.split('|')
        """seperates items in delivery reports and outputs those values to a list"""

        melon = relevant_report_values[0]#sets melon to value at idx [0]
        count = relevant_report_values[1]#sets relevant to value at idx [1]
        price = relevant_report_values[2]#sets price to value at idx [2]

        print(f"Delivered {count} {melon}s for a total of ${price}.")
    delivery_report.close() 
    """Outputs the delivery report in the proper order"""


dates_of_interest = ["20140519", "20140520", "20140521"]
"""sets the input values"""
for date in dates_of_interest:
    """Iterates through the produce_summary_report function for all input values"""
    produce_summary_report(date)