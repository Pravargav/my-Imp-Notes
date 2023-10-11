import random
import json


aNs = []

qIds = [
        "Q10",
        "Q11",
        "Q12",
        "Q13",
        ]

dIds = [
"03-1035142",
"04-0441690",
"04-4285561",
"05-6143552",
"06-5660716",
"06-6782906",
"08-4199851",
"08-8098224",
]

num = 57
answers = []


for i in range(num):
    aN = {
        "DOCTORID": random.choice(dIds),
        "QUESTIONID": random.choice(qIds),
        "ANSWERID": f"A{i+172}",
        "TEXT": random.choice(aNs),
        "VOTES": random.randint(0, 50),
    }
    answers.append(aN)


json_data = json.dumps(answers, indent=2)


print(json_data)
