import random
import datetime
import math

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def get_city(self):
        return self.city

class Profile:
    def __init__(self, username, address):
        self.username = username
        self.address = address

    def get_address(self):
        return self.address

class User:
    def __init__(self, name, email, profile):
        self.name = name
        self.email = email
        self.profile = profile

    def get_profile(self):
        return self.profile

# Long Message Chain
def get_user_city(user):
    return user.get_profile().get_address().get_city()

# Long parameter list
def create_invoice(user_id, product_id, amount, currency, tax, discount, due_date, notes):
    invoice = {
        "user_id": user_id,
        "product_id": product_id,
        "amount": amount,
        "currency": currency,
        "tax": tax,
        "discount": discount,
        "due_date": due_date,
        "notes": notes
    }
    return invoice

# Member ignoring method
class Report:
    def __init__(self, title):
        self.title = title

    def compute_average(self, values):  # <- No 'self'
        return sum(values) / len(values)

    def build_summary(self):  # Uses string concatenation in loop
        summary = ""
        for i in range(10):
            summary += "Report line " + str(i) + "\n"  # <- Smell
        return summary

# More long parameter list
def register_user(name, email, password, birthdate, phone, country, region, preferences):
    print(f"Registered {name} ({email}) from {country}/{region}")

def process_data(data):
    log = ""
    for item in data:
        log += "Processed: " + str(item) + "\n"  # <- Smell
    return log

class Logger:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(f"[{datetime.datetime.now()}] {entry}")

    def get(self):
        return "\n".join(self.entries)

# Another long message chain
def get_logger_time(log):
    return log.entries[-1].split("]")[0].strip("[")

# Another member-ignoring method
class Utils:
    def log_sum(a, b):  # <- Smell
        print(f"Sum: {a + b}")

def long_loop_concat():
    s = ""
    for i in range(100):
        s += str(i) + ","  # <- Smell
    return s

# Long message chain again
class Engine:
    def get_status(self):
        return "OK"

class Car:
    def __init__(self):
        self.engine = Engine()

    def get_engine(self):
        return self.engine

class Driver:
    def __init__(self):
        self.car = Car()

    def get_car(self):
        return self.car

def get_driver_engine_status(driver):
    return driver.get_car().get_engine().get_status()

# Useless member-ignoring method
class MathOps:
    def multiply(a, b):  # <- Smell
        return a * b

# Sample usage
if __name__ == "__main__":
    addr = Address("123 Main", "Toronto", "M1X1X1")
    prof = Profile("jdoe", addr)
    user = User("Jane", "jane@example.com", prof)

    print("City:", get_user_city(user))

    invoice = create_invoice(1, 101, 299.99, "CAD", 0.13, 5.00, "2025-08-01", "None")
    print("Invoice:", invoice)

    register_user("John", "john@example.com", "secret", "2000-01-01", "1234567890", "Canada", "ON", {"email_opt_in": True})

    report = Report("Monthly")
    print(report.build_summary())

    logger = Logger()
    logger.add("System started")
    logger.add("User login")
    print(logger.get())

    data = list(range(10))
    print(process_data(data))

    print(long_loop_concat())

    driver = Driver()
    print("Engine status:", get_driver_engine_status(driver))

    print("Logger time:", get_logger_time(logger))

    print("Multiply 5 * 6 =", MathOps.multiply(5, 6))
    print("Avg of [3, 4, 5] =", Report.compute_average([3, 4, 5]))
