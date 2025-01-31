def unique(elements):
    for i in range(len(elements) - 1):
        if elements[i] in l:
            continue
        else:
            l.append(elements[i])
l = []
elements = list(map(int, input("Enter elements separated by spaces: ").split()))
unique(elements)
print(l)