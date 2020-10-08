with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

# dict inside of dict
characteristics = {
    "hair_color": {
        "black": "CCAGCAATCGC",
        "brown": "GCCAGTGCCG",
        "blonde": "TTAGCTATCGC"
    },
    "facial_shape": {
        "square": "GCCACGG",
        "round": "ACCACAA",
        "oval": "AGGCCTCA"
    },
    "eye_color": {
        "blue": "TTGTGGTGGC",
        "green": "GGGAGGTGGC",
        "brown": "AAGTAGTGAC"
    },
    "gender": {
        "female": "TGAAGGACCTTC",
        "male": "TGCAGGAACTTC"
    },
    "race": {
        "white": "AAAACCTCA",
        "black": "CGACTACAG",
        "asian": "CGCGGGCCG"
    }
}

suspects = {
    "Eva": {
        "gender": "female",
        "race": "white",
        "hair_color": "blonde",
        "eye_color": "blue",
        "face_shape": "oval"
    },
    "Larisa": {
        "gender": "female",
        "race": "white",
        "hair_color": "brown",
        "eye_color": "brown",
        "face_shape": "oval"
    },
    "Matej": {
        "gender": "male",
        "race": "white",
        "hair_color": "black",
        "eye_color": "blue",
        "face_shape": "oval"
    },
    "Miha": {
        "gender": "male",
        "race": "white",
        "hair_color": "brown",
        "eye_color": "green",
        "face_shape": "square"
    }

}

persons = []

for i in characteristics["gender"]: # go trough gender dict keys
    gender = characteristics["gender"][i] # get value from very key in gender dict

    if gender in dna:
        print("Your suspect is {0}.".format(i))  #print key from finded value in dna

        for name in suspects:
            if suspects[name]["gender"] == "male":
                persons.append(name)
                print("Suspect based on gender: {0}".format(name))

# check if only one suspect
if len(persons) == 1:
    print("{0} ate the ice cream!".format(persons[0]))

for x in characteristics["eye_color"]:
    eye_color = characteristics["eye_color"][x]

    if eye_color in dna:
        print("Color of eyes: {0}".format(x))
        for person in persons:
            if suspects[person]["eye_color"] != x:
                persons.remove(person)

if len(persons) == 1:
    print("{0} ate the ice cream!".format(persons[0]))


