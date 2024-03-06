import random as rdm

censorValue = "";
chances = 7; 
sameCharacterIndices = [];
tempList = []

words = {
    "animal": "zebra",
    "fruit": "banana",
    "color": "blue",
    "vehicle": "car",
    "country": "France",
    "city": "Tokyo",
    "food": "pizza",
    "sport": "soccer",
    "movie": "Titanic",
    "book": "Harry Potter",
    "person": "Albert Einstein",
    "planet": "Mars",
    "element": "oxygen",
    "insect": "butterfly",
    "flower": "rose",
    "tree": "oak",
    "bird": "eagle",
    "fish": "salmon",
    "reptile": "snake",
    "amphibian": "frog",
    "invertebrate": "jellyfish",
    "mammal": "elephant",
    "rodent": "mouse",
    "dinosaur": "Tyrannosaurus",
    "fruit": "apple",
    "color": "green",
    "vehicle": "bicycle",
    "country": "Italy",
    "city": "Paris",
    "food": "sushi",
    "sport": "basketball",
    "movie": "The Godfather",
    "book": "The Lord of the Rings",
    "person": "Leonardo da Vinci",
    "planet": "Earth",
    "element": "carbon",
    "insect": "ant",
    "flower": "sunflower",
    "tree": "pine",
    "bird": "sparrow",
    "fish": "trout",
    "reptile": "turtle",
    "amphibian": "salamander",
    "invertebrate": "spider",
    "mammal": "lion",
    "rodent": "hamster",
    "dinosaur": "Velociraptor",
    "fruit": "orange",
    "color": "red",
    "vehicle": "motorcycle",
    "country": "Spain",
    "city": "London",
    "food": "pasta",
    "sport": "tennis",
    "movie": "Inception",
    "book": "1984",
    "person": "Marie Curie",
    "planet": "Jupiter",
    "element": "hydrogen",
    "insect": "bee",
    "flower": "tulip",
    "tree": "maple",
    "bird": "hawk",
    "fish": "goldfish",
    "reptile": "crocodile",
    "amphibian": "newt",
    "invertebrate": "snail",
    "mammal": "whale",
    "rodent": "rat",
    "dinosaur": "Stegosaurus",
    "fruit": "grape",
    "color": "yellow",
    "vehicle": "plane",
    "country": "Germany",
    "city": "New York",
    "food": "burger",
    "sport": "golf",
    "movie": "The Shawshank Redemption",
    "book": "To Kill a Mockingbird",
    "person": "Isaac Newton",
    "planet": "Saturn",
    "element": "gold",
    "insect": "dragonfly",
    "flower": "daisy",
    "tree": "palm",
    "bird": "penguin",
    "fish": "swordfish",
    "reptile": "lizard",
    "amphibian": "toad",
    "invertebrate": "octopus",
    "mammal": "tiger",
    "rodent": "squirrel",
    "dinosaur": "Brachiosaurus"
};

hintList = list(words.keys());
valueList = list(words.values());

# Grab index from the Dictonary
index = rdm.choice(range(len(hintList)));

# Grab the hint of corresponding index from the Dictonary
hint = hintList[index];

# Grab the value of corresponding index from the Dictonary
value = valueList[index];

# Censor the value
for censor in range(len(value)):
    censorValue += "*"; 

# Convert value into an array of characters
listOfLetters = list(value);
letterCount = 0;
index = 0; 
charPosition = 0;

print(value)
while (True):
    char = input("Guess a character or the word: ");
    # Censoring and uncensoring mechanism
    for letter in listOfLetters:
        if letter == char:
            tempList.append(letter)
        else:
            tempList.append("*")      
    listOfLetters = tempList; 

    print(listOfLetters);
    break    

# for letter in listOfLetters:
#         if (letter == char):
#             sameCharacterIndices.append(charPosition);
#             index += 1;
#         charPosition += 1;
# make a for loop and then save the index of the repeating characters using the for loop 
# for (i=0; i<5; i++) {
#   for (j=0; j<5; j++) {
#       if (chars[i] == value) {
#       	tempArray[j] = i; 
#       }
#   }
# }
# make an array to store all the indices value in the array. 
