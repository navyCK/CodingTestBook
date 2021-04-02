word = input().upper()          # missisipi
count_array = []
word_list = list(set(word))

for i in word_list:
    count = word.count(i)
    count_array.append(count)

if count_array.count(max(count_array)) >= 2:
    print("?")
else:
    print(word_list[count_array.index(max(count_array))])