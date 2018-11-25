import random

current_first_names = ["Sophia",  "Jackson",  "Emma",  "Aiden",  "Olivia",  "Lucas",  "Ava", \
"Liam",  "Mia",  "Noah",  "Isabella",  "Ethan",  "Riley",  "Mason",  "Aria",  "Caden",  "Zoe", \
"Oliver",  "Charlotte",  "Elijah",  "Lily",  "Grayson",  "Layla",  "Jacob",  "Amelia",  "Michael", \
"Emily",  "Benjamin",  "Madelyn", \
"Carter",  "Aubrey",  "James",  "Adalyn", \
"Jayden",  "Madison",  "Logan",  "Chloe",  "Alexander",  "Harper",  "Caleb",  "Abigail", \
"Ryan",  "Aaliyah",  "Luke",  "Avery",  "Daniel",  "Evelyn",  "Jack",  "Kaylee",  "William", \
"Ella",  "Owen",  "Ellie",  "Gabriel",  "Scarlett",  "Matthew",  "Arianna",  "Connor",  "Hailey", \
"Jayce",  "Nora",  "Isaac",  "Addison",  "Sebastian",  "Brooklyn",  "Henry",  "Hannah",  "Muhammad",  "Mila",\
"Cameron",  "Leah",  "Wyatt",  "Elizabeth",  "Dylan",  "Sarah",  "Nathan",  "Eliana",  "Julian",  "Mackenzie", \
"Eli",  "Peyton",  "Levi",  "Maria",  "Isaiah",  "Grace",  "Landon",  "Adeline",  "David",  "Elena",  "Christian", \
"Anna",  "Andrew",  "Victoria",  "Brayden",  "Camilla",  "John",  "Lillian"]

def get_names(male = False, rand = True, names = current_first_names):
    if rand:
        names = [name for index, name in enumerate(current_first_names) if (index % 2 != 0 and male) or (index % 2 == 0 and not male)]
        return random.choice(names)
    return (name for index, name in enumerate(current_first_names) if index % 2 != 0)

print(get_names())

# def first_name(names = current_first_names):
