from user_generator import UserGenerator
from common import generate_csv

if __name__ == "__main__":
    generate_csv(UserGenerator, ["uuid", "name", "gender", "birthdate", "age", "address"], 100, "data/users.csv")