
rules = [
    {
        "rule": "R1",
        "conditions": ["high_fever", "headache"],
        "diagnosis": "Fever"
    },
    {
        "rule": "R2",
        "conditions": ["sneezing", "runny_nose", "sore_throat"],
        "diagnosis": "Common Cold"
    },
    {
        "rule": "R3",
        "conditions": ["high_fever", "body_ache", "fatigue"],
        "diagnosis": "Flu"
    },
    {
        "rule": "R4",
        "conditions": ["cough", "mild_fever"],
        "diagnosis": "Common Cold"
    },
    {
        "rule": "R5",
        "conditions": ["chills", "high_fever"],
        "diagnosis": "Flu"
    }
]

temperature = float(input("Enter body temperature (°C): "))

print("Enter symptoms separated by commas")
print("Example: chills, body_ache, fatigue\n")

user_input = input("Symptoms: ").lower()
user_symptoms = user_input.split(",")

for i in range(len(user_symptoms)):
    user_symptoms[i] = user_symptoms[i].strip()

if temperature > 38:
    user_symptoms.append("high_fever")
elif temperature >= 37 and temperature <= 38:
    user_symptoms.append("mild_fever")


fired_rules = []
diagnoses = []

for rule in rules:
    match = True
    for condition in rule["conditions"]:
        if condition not in user_symptoms:
            match = False
            break

    if match:
        fired_rules.append(rule["rule"])
        diagnoses.append(rule["diagnosis"])

print("\n Diagnosis Result ")

if len(diagnoses) > 0:
    final_diagnosis = max(set(diagnoses), key=diagnoses.count)
    print("Identified Disease:", final_diagnosis)
    print("Matched Rules:", ", ".join(fired_rules))
    print("Advisory: Please consult a doctor.")
else:
    print("No disease could be identified.")
    print("Advisory: Please consult a doctor for further examination.")
