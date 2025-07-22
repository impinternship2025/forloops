from pharmacy import Pharmacy
from customer import Customer

def main():
    users = {
        "admin": {"password": "admin123", "role": "admin"},
        "customer1": {"password": "cust123", "role": "customer"}
    }

    pharmacy = Pharmacy()

    
    pharmacy.add_medicine("Paracetamol", "tablet", 50, 10.0)
    pharmacy.add_medicine("Cough Syrup", "syrup", 30, 45.5)
    pharmacy.add_medicine("Skin Ointment", "ointment", 20, 75.0)

    print("Welcome to the Pharmacy Management System")

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = users.get(username)
        if user and user["password"] == password:
            print(f"\nLogin successful! Welcome {username} ({user['role']})")
            break
        else:
            print("Invalid username or password. Try again.\n")

    if user["role"] == "admin":
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add Medicine")
            print("2. View Medicines")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter medicine name: ")
                med_type = input("Enter medicine type (tablet/syrup/ointment): ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price per unit: ₹"))
                pharmacy.add_medicine(name, med_type, quantity, price)
            elif choice == "2":
                pharmacy.view_medicines()
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")

    elif user["role"] == "customer":
        customer = Customer(username)
        while True:
            print("\n--- Customer Menu ---")
            print("1. Buy Medicine")
            print("2. View Purchase Summary")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                med_name = input("Enter medicine name to buy: ")
                med_type = input("Enter medicine type: ")
                quantity = int(input("Enter quantity: "))
                pharmacy.buy_medicine(customer, med_name, med_type, quantity)
            elif choice == "2":
                customer.view_purchases()
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()