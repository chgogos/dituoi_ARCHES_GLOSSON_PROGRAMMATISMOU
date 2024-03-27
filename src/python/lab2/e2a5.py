from faker import Faker

fake = Faker()
Faker.seed(42)

def generate_fake_person():
    name = fake.name()
    address = fake.address().replace('\n', ', ')
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
    return f"{name};{address};{birthdate}"

def generate_fake_persons(num_persons=100):
    persons = []
    for _ in range(num_persons):
        person = generate_fake_person()
        persons.append(person)
    return persons

def write_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for person in data:
            file.write(person + '\n')

if __name__ == "__main__":
    num_persons = 100
    fake_persons = generate_fake_persons(num_persons)
    filename = 'fake100.txt'
    write_to_file(fake_persons, filename)
    print(f"Δημιουργία στοιχείων {num_persons} υποθετικών ατόμων και αποθήκευση στο αρχείο {filename}.")
