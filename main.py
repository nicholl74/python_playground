"""Just learning some Python"""
#Ranking the top 5 words in a file

fhand = open("C:\\Users\\Mark\\Desktop\\python_files\\intro.txt")

counts = dict()

for line in fhand:
    words = line.split()
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

