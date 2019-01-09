name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
counts = dict()    
handle = open(name)
for line in handle:
    if line.startswith('From:'):
        #print(line)
        words = line.split()
        email = words[1]
        #print(email)
        if email not in counts:
            counts[email] = 1
        else:
            counts[email] = counts[email] + 1   
max_num = 0
email_name = None
#print(counts)
values = list(counts.values())
keys = list(counts.keys())
#print(values)
#print(keys)
position = 0
for index in range(len(values)):
    if values[index] > max_num:
        max_num = values[index]
        position = index
        
print(keys[position], values[position])

"""
for key in counts:    
	if counts[key] > max_num :       
    	max_num = counts[key]
"""              
#print('cwen@iupui.edu', max_num)