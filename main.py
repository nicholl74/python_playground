"""Just learning some Python"""

fhand = open("C:\\Users\\Mark\\Desktop\\python_files\\intro.txt")

counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(f'Word count - {counts}')
