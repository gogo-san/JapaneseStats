import os
import re
import json

jlpt_result = dict()
jlpt_count = dict()
for i in range(1,6):
    jlpt_count.setdefault(i,0)

f = open("jlpt_vocalbulary.txt",encoding='utf-8')
while(1):
    line = f.readline()
    if line == "":
        break
    key = re.search( r"div style=\'font-family: Arial; font-size: 20px;\'>(.*?)</div>", line).groups()[0]
    value = re.search(r"N([1-5])",line).groups()[0]
    print(key,value)
    jlpt_result[key] = value
    jlpt_count[int(value)] += 1

f.close()
print(jlpt_result)
print(jlpt_count)   

with open("jlpt.json",'w') as json_file:
    json.dump(jlpt_result,json_file)