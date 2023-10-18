"""
customer_invoice.py: Checkout for a cusotmer and display. Then save the invoice dated text file as well.

By: V. Miranda-Calleja

11/29/2021
"""

def main():

    #ask user to enter current date to generate a test file name
    date = input("Enter today's date in the format of ddmmyyyy: ")
    invoice_file_name = "Inovice_" + date + ".txt"

    #create a file object to write invoice details into the text file
    #try/except/else even if some parts don't work it will still print of no errors
    try:
        to_file = open(invoice_file_name, "w")
    except IOError:
        print("Cannot save the invoice to the specified file")
    else: #When no error raised, thje program flows with this block
        total_quantity = 0
        grandtotal = 0

        more_item = input("Enter y if the customer is ready to checkout: ")
        while more_item == "y":
            #fucntion for item details
            item_name, price, quantity = checkout_item()
            subtotal = price * quantity
            total_quantity += quantity
            grandtotal += subtotal
            #each iteration saves details to files
            save_item_to_file(to_file, item_name, price, quantity, subtotal)

            more_item = input("Enter y to checkout next item or Enter any other key to stop: ")

        #save total quantity and grand_total to the same file
        save_summary_to_file(to_file, total_quantity, grandtotal)

        #close the file
        to_file.close()

        print_reciept(invoice_file_name)

#line 28
def checkout_item():
    name = input("Enter item's name: ")
    price = float(input("Enter item's price: "))
    count = int(input("Quantity: "))
    #return in same order as in main()
    return name, price, count

#line 33
def save_item_to_file(file_object, name, unit_price, count, total):
            #\t // \n : escape characters
    file_object.write(name + "\t\t$" + str(unit_price) + "\t*\t" + str(count) + "\t\t$" + str(total) + "\n")

#line 38
def save_summary_to_file(file_object, total_count, grand_total):
    file_object.write("\n\n")
    file_object.write("-------Summary-------\n")
    file_object.write("Total Counts: " + str(total_count) + "\n")
    file_object.write("Total Amount Due: $" + str(grand_total) + "\n\n\n")
    file_object.write("Thank you for Shopping with us!")

def print_reciept(file_name):
    try:
        from_file = open(file_name, 'r')
    except:
        print("File cannot be opened")
    else:
        reciept = from_file.read()
        print(reciept)
        from_file.close()

main()
