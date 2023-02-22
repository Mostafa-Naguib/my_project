import re



while True:
    email = input("Email: ").strip()
    checker = re.search("^(\w+)@(\w+)\.(com|net|org|info)$", email)
    if checker:
        break    


print(f"User name: {checker.group(1)}")
print(f"Domain: {checker.group(2)}")
print(f"Top Level Domain: {checker.group(3)}")
