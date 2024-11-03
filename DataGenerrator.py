import csv
import random
import uuid
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for generating names
fake = Faker()

# Function to generate random date within the last year
def generate_random_datetime():
    start_date = datetime.now() - timedelta(days=365)  # Approx 1 year back
    random_days = random.randint(0, 365)
    random_date = start_date + timedelta(days=random_days)
    # Generate random time: hours, minutes, and seconds
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    # Combine date and time
    random_datetime = random_date.replace(hour=random_hour, minute=random_minute, second=random_second)
    
    return random_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Function to generate random donation amount
def generate_donation_amount():
    return round(random.uniform(10, 1000), 2)  # Donation amount between $10 and $1000

# Function to randomly select preferred language
def generate_preferred_language():
    return random.choice(['EN', 'FR'])

# Function to randomly select transaction type and determine amount
def generate_transaction():
    weights = [0.7, 0.3] 
    transaction_type = random.choices(['Donation', 'Membership'], weights=weights, k=1)[0]
    amount = 15.00 if transaction_type == 'Membership' else generate_donation_amount()
    return transaction_type, amount

# Function to randomly select preferred salutation
def generate_preferred_salutation():
    return random.choice(['Mr', 'Mrs/Ms'])

# Function to randomly select preferred payment platform
def generate_preferred_platform():
    return random.choice(['Mastercard', 'Visa'])

# Function to randomly select preferred Province
def generate_preferred_province():
    return random.choice(['ON', 'BC', 'AB', 'QC', 'NL', 'SK', 'MB', 'NS', 'NB', 'PE', 'NT', 'YT', 'NU'])

# Function to randomly select preferred Campaign
def generate_preferred_campaign():
    return random.choice(['SaveTheKids', 'AbuseVictims', 'GalaNight', 'SpeedDating', 'DogWalking', 'IceBucket'])

# Function to generate a unique transaction ID
def generate_transaction_id():
    return str(uuid.uuid4())

# Function to randomly generate transaction status
def generate_preferred_status():
    weights = [0.8, 0.2] 
    return random.choices(['Success', 'Failed'],weights=weights, k=1)[0]


# Number of records to generate
num_records = 25000

# Create CSV file with random data
with open('random_transactions.csv', 'w', newline='') as csvfile:
    fieldnames = ['Transaction ID', 'DateTime', 'Name', 'TransactionType', 'Amount', 'Preferred Language', 'Salutation', 'Platform', 'Province', 'Campaign', 'Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for _ in range(num_records):
        transaction_type, amount = generate_transaction()
        writer.writerow({
            'Transaction ID': generate_transaction_id(),
            'DateTime': generate_random_datetime(),
            'Name': fake.name(),
            'TransactionType': transaction_type,
            'Amount': amount,
            'Preferred Language': generate_preferred_language(),
            'Salutation': generate_preferred_salutation(),
            'Platform': generate_preferred_platform(),
            'Province': generate_preferred_province(),
            'Campaign': generate_preferred_campaign(),
            'Status': generate_preferred_status()
        })

print("CSV file 'random_transactions.csv' has been created with 25000 records.")
