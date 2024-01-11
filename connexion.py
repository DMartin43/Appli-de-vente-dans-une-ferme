def find_pairs(input_list, target):
    pairs = []
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[i] + input_list[j] == target:
                pairs.append((i, j))
    return pairs

# Exemple d'utilisation
user_list = list(map(int, input("Entrez les entiers de la liste, séparés par des espaces : ").split()))
user_target = int(input("Entrez la valeur cible : "))
result = find_pairs(user_list, user_target)
print("Les paires d'indices d'éléments de la liste dont la somme est égale à la valeur cible sont :", result)