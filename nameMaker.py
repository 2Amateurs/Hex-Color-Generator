import random

adjectives=["dead","putrid","radioactive","Sam wins","Katie loses","glittery","smurfy","let it die","not-on-time","hot dog","fruit acid","didn't think","fabulous","edible","don't eat it","rocky","fantastic","spelled correctly","Sam loses","Katie wins","offended","in disguise"]

nouns=["blue","yellow","magenta","green","brown","turquoise","white","red","orange","gray","black","scarlet","mustard","ketchup","pumpkin","who-knows","dirt","purple","violet","indigo","maroon","skunk","giraffe","baby","insect","cell tissue","garbage","lorax","sparkly pink"]

def getName():
    value1 = random.randint(0, len(adjectives)-1)
    value2 = random.randint(0, len(nouns)-1)
    print(adjectives[value1] + " " + nouns[value2])
