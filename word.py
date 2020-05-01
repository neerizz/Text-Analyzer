file_obj = open(r'hitch3.txt','r')

word_string = file_obj.read()

word_list = word_string.split()

word_list_final=[]

def islegal(s):
    if s.isdigit():
        return True
    for j in range(len(s)):
        if(s[j].isalpha() or s[j].isdigit() or s[j]=='-' or s[j]=='\''):
            continue
        else:
            s1 = s.replace(s[j]," ")
            s=s1
        word_list[i]=s1
    return True

for i in range(len(word_list)):
    a = islegal(word_list[i])
    if a :
        word_list_final.append(word_list[i])
    else:
        continue

for i in range(len(word_list_final)):
    word_list_final[i] = word_list_final[i].strip()
    
while "" in word_list_final:
    word_list_final.remove("")

for i in range(len(word_list_final)):
    word_list_final[i] = word_list_final[i].lower()

#iske neeche most popular ka code hai
temp_list = sorted(word_list_final,key=word_list_final.count,reverse=True)

freq = {} 

def CountFrequency(temp_list): 
    for item in temp_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1

CountFrequency(temp_list)

with open(r"most_popular.txt",'w') as file:
    for key,value in freq.items():
        file.writelines("%s : %d\n"%(key,value))

#Alphabetical wala code

temp_list2 = sorted(word_list_final)

frequency={}

def CountFrequency1(temp_list): 
    for item in temp_list: 
        if (item in frequency): 
            frequency[item] += 1
        else: 
            frequency[item] = 1

CountFrequency1(temp_list2)

with open(r"Alphabetical.txt",'w') as file:
    for key,value in frequency.items():
        file.writelines("%s : %d\n"%(key,value))