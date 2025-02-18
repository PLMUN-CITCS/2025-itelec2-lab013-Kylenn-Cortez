# Kylenn Rhyss Cortez
# ITELEC2
# Laboratory # 13 - Guided Coding Exercise: for Loop with break and continue

def main():
    numbers = list(range(1, 11))
    for num in numbers:
            if num == 3:
                continue  # Skip the rest of this iteratio
            if num == 7:
                break  # Exit the loop completely
            print(num)
if __name__ == "__main__":
    main()
