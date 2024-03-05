import random as rdm

censorValue = "";
chances = 7; 
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

for censor in range(len(value)):
    censorValue += "*"; 
