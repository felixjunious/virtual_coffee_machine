````markdown
# ☕ Virtual Coffee Machine

A fully functional **virtual coffee machine simulator** written in Python.  
It simulates how a real coffee machine works — tracking ingredients, processing payments, managing inventory, and providing an admin mode for maintenance tasks.

This project was built for self-learning purposes and demonstrates:
- Object-oriented programming  
- Modular Python design  
- Dataclasses  
- Handling user input  
- Simulating a real machine workflow  

---

## 🚀 Features

### 👤 User Features
- Order drinks by name  
- Insert coins in EUR (1c → 2€)  
- Automatic change calculation  
- Ingredient availability checks  
- Coffee is “brewed” if resources and payment are sufficient  
- Machine reports for:
  - Water
  - Milk
  - Coffee grounds
  - Revenue

### 🔧 Admin Features
Accessible only through a password prompt.

- Refill machine resources  
- Add new menu items  
- Remove menu items  
- View ingredient costs  
- Manually adjust revenue  
- Full system report  

---

## 🧩 Project Structure

```text
virtual_coffee_machine/
│
├── main.py
├── coffee_machine.py
├── money_machine.py
├── menu.py
├── admin.py
├── README.md
└── LICENSE
````

### **`coffee_machine.py`**

Handles:

* Resource tracking
* Resource validation
* Brewing coffee
* Reporting
* Refilling ingredients

### **`money_machine.py`**

Handles:

* EUR coin system
* Coin input
* Payment processing
* Revenue tracking

### **`menu.py`**

Handles:

* Menu items using `@dataclass`
* Adding/removing drinks
* Finding drinks
* Displaying menu

### **`admin.py`**

Handles:

* Password authentication
* Admin menu options
* Resource modifications
* Menu management

---

## 🖥️ How to Run

### **1. Clone the repository**

```sh
git clone https://github.com/felixjunious/virtual_coffee_machine
cd virtual_coffee_machine
```

### **2. Run the program**

```sh
python main.py
```

---

## 🧪 Example Usage

```
--- Virtual Coffee Machine ---
Espresso     - €1.50
Latte        - €2.50
Cappuccino   - €3.00

What would you like? latte

Insert coins:
2€: 1
1€: 0
50c: 1
...

Here is your Latte ☕ Enjoy!
```

Admin mode example:

```
Enter admin password:
> admin123
Access granted.

1. Refill ingredients
2. Add menu item
3. Remove menu item
4. Modify revenue
5. View system report
```

---

## 🔮 Future Improvements

Possible enhancements:

* Logging system
* Saving state to JSON
* GUI version (Tkinter or PyQt)

---


