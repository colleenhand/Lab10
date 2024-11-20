#The authors' names are: Colleen and Anna
names = ["Margaret", "Laneman", "Lily", "DeYoung", "Serenity", "Schuler", "Olivia", "Beck", "Colleen", "Hand", "Anna", "Raycroft", "Victoria", "Garcia Jimenez", "Gwyneth", "Gangwer", "Mairi", "Weber-Hess", "Aliza", "Litvak", "Elizabeth", "Wyatt", "Rylee", "Taylor"]
frequency_names = dict()
for x in names[1::2]:
    if x[0] not in frequency_names:
        frequency_names[x[0]] = 1
    else:
        frequency_names[x[0]] += 1
print(frequency_names)
