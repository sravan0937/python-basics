from dotenv import load_dotenv
import os

result = load_dotenv(dotenv_path="basics.env")
print("Loaded:", result)

pwd = os.getenv("password")
print("Password from .env:", pwd)









