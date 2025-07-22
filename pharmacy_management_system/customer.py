class Customer:
    def __init__(self, name):
        self.name = name
        self.purchases = []  

    def view_purchases(self):
        if not self.purchases:
            print("You have not purchased any medicines yet.")
            return
        
        print(f"\nPurchase Summary for {self.name}:")
        count = 1
        for med in self.purchases:
            total_price = med.price * med.quantity
            print(f"{count}. {med.name} - Type: {med.med_type} - Quantity: {med.quantity} - Unit Price: ₹{med.price} - Total: ₹{total_price}")
            count += 1
