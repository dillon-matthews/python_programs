with open("treeData.txt", "r") as file:
    lines = file.readlines()

tree_data = []
for line in lines[1:]:
    parts = line.strip().split(", ")
    tree_id = int(parts[0])  
    genus_species = parts[1]
    common_name = parts[2]
    family = parts[3]
    tree_data.append((tree_id, genus_species, common_name, family))

sorted_by_tree_id = sorted(tree_data, key=lambda x: x[0])
print("Sorted by Tree ID:")
for tree in sorted_by_tree_id:
    print(tree)

sorted_by_family = sorted(tree_data, key=lambda x: x[3])
print("\nSorted by Family:")
for tree in sorted_by_family:
    print(tree)
