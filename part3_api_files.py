import requests
from datetime import datetime

# ---------------- TASK 1 ----------------

# writing file
with open("python_notes.txt", "w", encoding="utf-8") as f:
    f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    f.write("Topic 2: Lists are ordered and mutable.\n")
    f.write("Topic 3: Dictionaries store key-value pairs.\n")
    f.write("Topic 4: Loops automate repetitive tasks.\n")
    f.write("Topic 5: Exception handling prevents crashes.\n")

print("File written successfully")

# appending
with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions help reuse code.\n")
    f.write("Topic 7: APIs allow communication between systems.\n")

print("Lines appended")

# reading
with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    print(f"{i}. {line.strip()}")

print("Total lines:", len(lines))

keyword = input("Enter keyword: ").lower()
found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No match found")


# ---------------- TASK 2 ----------------

try:
    res = requests.get("https://dummyjson.com/products?limit=20", timeout=5)
    data = res.json()
    products = data["products"]

    print("\nProducts List:")
    for p in products:
        print(p["id"], p["title"], p["category"], p["price"], p["rating"])

except Exception as e:
    print("API Error:", e)


# filter + sort
filtered = [p for p in products if p["rating"] >= 4.5]
filtered.sort(key=lambda x: x["price"], reverse=True)

print("\nFiltered:")
for p in filtered:
    print(p["title"], p["price"])


# laptops
try:
    res = requests.get("https://dummyjson.com/products/category/laptops", timeout=5)
    data = res.json()

    print("\nLaptops:")
    for p in data["products"]:
        print(p["title"], p["price"])

except Exception as e:
    print("Error:", e)


# post
try:
    new = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "test product"
    }

    res = requests.post("https://dummyjson.com/products/add", json=new)
    print("\nPOST:", res.json())

except Exception as e:
    print("Post error:", e)


# ---------------- TASK 3 ----------------

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


def read_file_safe(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
    finally:
        print("Done file check")

print(read_file_safe("python_notes.txt"))
read_file_safe("ghost.txt")


# ---------------- LOOP ----------------

while True:
    val = input("Enter product ID (1-100) or quit: ")

    if val.lower() == "quit":
        break

    if not val.isdigit():
        print("Enter valid number")
        continue

    val = int(val)

    if val < 1 or val > 100:
        print("Out of range")
        continue

    try:
        res = requests.get(f"https://dummyjson.com/products/{val}")

        if res.status_code == 200:
            data = res.json()
            print(data["title"], data["price"])
        else:
            print("Not found")

    except Exception as e:
        print("Error:", e)


# ---------------- TASK 4 ----------------

def log_error(fn, etype, msg):
    with open("error_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] {fn} {etype} {msg}\n")


# connection error
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except Exception as e:
    log_error("fetch", type(e).__name__, str(e))


# 404 error
res = requests.get("https://dummyjson.com/products/999")
if res.status_code != 200:
    log_error("lookup", "HTTPError", "404 product not found")


print("\nLog File:")
with open("error_log.txt", "r") as f:
    print(f.read())