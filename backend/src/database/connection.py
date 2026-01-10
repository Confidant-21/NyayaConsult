import os
from dotenv import load_dotenv

load_dotenv()   # 👈 THIS IS REQUIRED

DATABASE_URL = os.getenv("DATABASE_URL")




if DATABASE_URL:
    print("Connection Available!")
    print(DATABASE_URL)
else:
    print("Connection Not Available!!")