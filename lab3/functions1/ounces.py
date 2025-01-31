def weight():
    grams = int(input("How many grams you need for the ingredients: "))
    ounces = 28.3495231 * grams
    return ounces
print(weight())