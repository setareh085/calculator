# Calculator Project (Python)

This project demonstrates different implementations of a calculator using **Python**.  
It includes a **text-based CLI version**, an **object-oriented version**, a **GUI version with Tkinter**, and some **helper functions**.

---

## ✨ Features
- **CLI Calculator (`calculator.py`)**  
  Text-based calculator that interacts with the user through the terminal.  
  Uses the OOP and helper modules internally.
  
- **OOP Calculator (`calculator_oop.py`)**  
  Provides a `calculators` class to handle arithmetic operations using object-oriented programming.
  
- **GUI Calculator (`calculator_gui.py`)**  
  Graphical calculator built with the **Tkinter** library.  
  Supports number input, basic operations, clear function, and error handling.
  
- **Helper Functions (`to_check.py`)**  
  - `get_number(prompt)` → Ensures user enters a valid integer.  
  - `is_empty(lst)` → Checks if a list is empty.  

- **Main Runner (`run.py`)**  
  Provides a simple menu where the user can choose which calculator to run:
  - `1` → CLI calculator  
  - `2` → GUI calculator  
  - `3` → OOP calculator (can be extended)  
  - `4` → Test/Helper file  

---

## 🚀 Installation & Usage
1. Install **Python 3.x**.
2. Clone or download this repository.
3. Run the main menu:
   ```bash
   python run.py
    ```
4. The calculator window will appear and you can start using it.

## 📂 Project Structure
calculator/

│

├── calculator.py        # CLI calculator (uses OOP + helpers)

├── calculator_oop.py    # OOP calculator class

├── calculator_gui.py    # GUI calculator (Tkinter)

├── to_check.py          # Helper functions

├── run.py               # Main runner (menu)

├── README.md            # Project description

└── LICENSE              # License file

📝 License

This project is licensed under the MIT License
You are free to use, modify, and distribute it.
