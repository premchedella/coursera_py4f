name = input("Enter file:")
counts = dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith('From'):
        words = line.split()
        if (len(words)) > 2:
            time = words[5].split(":")
            hours = time[0]
            if hours not in counts:
            	counts[hours] = 1
            else:
            	counts[hours] = counts[hours] + 1
lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)