import os

# Arbitrary change
name = os.environ.get("WHO_TO_GREET", "GitHub Actions Student")

print(f"Hello {name}!")
print("This program is running inside GitHub Actions.")
