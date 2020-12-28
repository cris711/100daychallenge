class Order:
    def __init__(invoice,order_number,item_name,item_number,price):
        invoice.order_number = order_number
        invoice.item_name = item_name
        invoice.item_number = item_number
        invoice.price = price


    def print_total(invoice):
        print("Order Number: ", invoice.order_number)
        print("Item Name: ", invoice.item_name)
        print("Item Number: ", invoice.item_number)
        print("Item Price: $",invoice.price)

def main():
    
    order_1 = Order(1,"RAM",5,50) 
    order_1.print_total()
if __name__ == "__main__":
    main()
        
