
for i in range(1, 11):

  with open(f"/workspaces/Practice-Python/File IO/table{i}.txt", "w") as f:
    for j in range(1, 11):
         f.write(f" {i}x {j} = {i * j}\n")
