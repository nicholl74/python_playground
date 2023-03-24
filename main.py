"""Just learning some Python"""
# Ranking the top 5 words in a file
from pathlib import Path

fhand = open("C:\\Users\\Mark\\Desktop\\python_files\\intro.txt")
outf = open(Path.cwd() / Path('NewFolder') / "output.txt", "w")

#print(fhand.readlines())
counts = dict()


for line in fhand.readlines():
    words = line.split()
    outf.write(str(words))
    outf.write('\n')
    for word in words:
        counts[word] = counts.get(word, 0) + 1


print(f'Word count - {counts}')

lst = list()

for k, v in counts.items():
    lst.append((v, k))

lst.sort(reverse=True)

i = 1
for k, v in lst[:5]:
    print(f"At rank number {i} we have '{v}' with a total of {k} appearances")
    i += 1



