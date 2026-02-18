
is_a = {
    "Bird": "Animal",
    "Mammal": "Animal",
    "Sparrow": "Bird",
    "Dog": "Mammal"
}


can = {
    "Bird": ["fly"],
    "Mammal": ["walk"]
}


def can_do(entity, action, path):
    

    if entity in can and action in can[entity]:
        path.append(entity)
        return True

    
    if entity in is_a:
        path.append(entity)
        return can_do(is_a[entity], action, path)

    return False



query = input("Enter Query:\n").strip().lower()

parts = query.replace("?", "").split()
entity = parts[1].capitalize()
action = parts[2]

path = []
result = can_do(entity, action, path)

print()
if result:
    
    reasoning = " → ".join(path) + f" → can {action}"
    print("Yes")
    print(f"Reason: {reasoning}")
else:
    print("No")
    print("Reason: Knowledge not found")
