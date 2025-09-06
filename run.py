print("Choose mode:")
print("1. CLI (text calculator)")
print("2. GUI (window calculator)")

choice = input("your choice: ")

if choice == "1":
    import calculator   # فایل متنی
elif choice == "2":
    import calculator_gui  # فایل گرافیکی
