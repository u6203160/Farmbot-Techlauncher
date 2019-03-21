from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("EMAIL"))
print(os.getenv("PASSWORD"))
