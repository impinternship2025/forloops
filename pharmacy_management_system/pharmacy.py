from medicine import Medicine

class Pharmacy:
    def __init__(self):
        self.medicines = []
        self.orders = []

    def add_medicine(self, name, med_type, quantity, price):
        med = Medicine(name, med_type, quantity, price)
        self.medicines.append(med)
        print(f"Medicine '{name}' added successfully!")

    def view_medicines(self):
        if not self.medicines:
            print("No medicines in the pharmacy!")
            return

        print("\nList of Medicines:")
        count = 1
        for med in self.medicines:
            print(f"{count}. {med.name} - Type: {med.med_type} - Quantity: {med.quantity} - Price: ₹{med.price}")
            count += 1

    def buy_medicine(self, customer, med_name, med_type, quantity):
        for med in self.medicines:
            if med.name.lower() == med_name.lower() and med.med_type.lower() == med_type.lower():
                if med.quantity >= quantity:
                    total_cost = med.price * quantity
                    print(f"Total cost for {quantity} units of '{med.name}' is ₹{total_cost}")
                    
                    payment_method = input("Choose payment method (cash/card): ").strip().lower()
                    if payment_method not in ["cash", "card"]:
                        print("Invalid payment method selected. Purchase cancelled.")
                        return

                    
                    med.quantity -= quantity
                    purchased = Medicine(med.name, med.med_type, quantity, med.price)
                    customer.purchases.append(purchased)
                    self.orders.append((customer.name, purchased))
                    print(f"{quantity} units of '{med.name}' bought successfully by {customer.name} using {payment_method}!")
                    return
                else:
                    print(f"Only {med.quantity} units available, not enough stock.")
                    return
        print("Medicine not found in stock.")
