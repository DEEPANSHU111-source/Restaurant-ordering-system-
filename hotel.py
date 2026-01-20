import pyfiglet

class Hotel:
    def __init__(self):
        self.menu = {
            "1": ["Paneer Butter Masala", 250],
            "2": ["Chicken Biryani", 300],
            "3": ["Butter Naan", 30],
            "4": ["Coffee", 50],
            "5": ["Gulab Jamun", 80],
            "6": ["Veg Manchurian", 220],
            "7": ["Tandoori Chicken", 350],
            "8": ["Hakka Noodles", 180],
            "9": ["Fresh Lime Soda", 60],
            "10": ["Masala Chai", 40],
            "11": ["Mutton Rogan Josh", 400],
            "12": ["Palak Paneer", 240],
            "13": ["Dal Makhani", 190],
            "14": ["Plain Rice", 100],
            "15": ["Ice Cream (Vanilla)", 90],
            "16": ["Mango Lassi", 70],
            "17": ["Spring Rolls", 160],
            "18": ["Fish Curry", 380],
            "19": ["Veg Thali", 320],
            "20": ["Chicken Thali", 400]
        }

    def show_menu(self):
        print(pyfiglet.figlet_format("MENU", font="standard"))
        print("----- MENU -----")
        for key, item in self.menu.items():
            print(f"{key}. {item[0]} - ₹{item[1]}")

    def check_family_pack(self):
        answer = input("Are you with family (yes/no)? ").lower()
        if answer == "yes":
            print("Congrats! You got a 35% family pack discount!")
            return 35
        else:
            print("No worries, we are happy to serve you!")
            return 0
        


    def take_order(self, discount=0):
        print("\nEnter the item numbers and quantity (e.g. 1x2,3x1,5x4):")
        order_input = input("Your order: ").split(",")
        total = 0
        print("\n--- Order Summary ---")
        for item_entry in order_input:
            item_entry = item_entry.strip().lower()
            if 'x' in item_entry:
                item_num, qty = item_entry.split('x')
                item_num = item_num.strip()
                try:
                    qty = int(qty.strip())
                except ValueError:
                    print(f"Invalid quantity for item {item_entry}. Skipping.")
                    continue

                if item_num in self.menu:
                    name, price = self.menu[item_num]
                    item_total = price * qty
                    print(f"{name} x {qty} = ₹{item_total}")
                    total += item_total
                else:
                    print(f"Item {item_num} not found in the menu.")
            else:
                print(f"Invalid format for item: {item_entry} (use format like 1x2)")

        if discount > 0:
            print(f"\nSubtotal: ₹{total}")
            discount_amount = (discount / 100) * total
            total -= discount_amount
            print(f"Discount ({discount}%): -₹{int(discount_amount)}")

        print(f"Total Amount to Pay: ₹{int(total)}")
        print(pyfiglet.figlet_format("Thank You!", font="slant"))





print(pyfiglet.figlet_format("= Enter your username =", font="digital"))

banned_names = ["sahil", "faisal", "suhail", "asim"]


while True:
    first_name = input("Enter your First Name (required): ").strip()
    if not first_name.isalpha():
        print("❌ First name should contain letters only.")
    elif first_name.lower() in banned_names:
        print("🚫 Sorry, you are not allowed to enter the restaurant.")
        exit()
    else:
        break


while True:
    middle_name = input("Enter your Middle Name (optional): ").strip()
    if middle_name == "":
        break
    elif not middle_name.isalpha():
        print("❌ Middle name should contain letters only.")
    else:
        break


while True:
    last_name = input("Enter your Last Name (optional): ").strip()
    if last_name == "":
        break
    elif not last_name.isalpha():
        print("❌ Last name should contain letters only.")
    else:
        break

full_name = f"{first_name} {middle_name + ' ' if middle_name else ''}{last_name}".strip()
print(f"\n✅ Welcome, {full_name}!")


print(pyfiglet.figlet_format("= Enter your mobile number =", font="digital"))

while True:
    mobile = input("Mobile = ")
    if mobile.isdigit() and len(mobile) == 10:
        break
    else:
        print("❌ Invalid mobile number. Please enter exactly 10 digits (numbers only).")


print(pyfiglet.figlet_format("Welcome to THE OBEROI", font="standard"))

print("Are you a 'regular' user or a 'new' user?")
answer = input("Input here = ").lower()


if answer == "regular":
    print("Thanks for visiting the hotel again")
    print(pyfiglet.figlet_format("Congrats", font="bubble"))
    print("You got 20 percent discount!")
    discount = 20
else:
    print("Welcome to THE OBEROI")
    print("You are a new customer")
    print("You get 30 percent discount!")
    discount = 30

hotel = Hotel()


family_discount = hotel.check_family_pack()


final_discount = max(discount, family_discount)

hotel.show_menu()
hotel.take_order(discount=final_discount)
