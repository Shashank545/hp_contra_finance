import re

with open("Talend_Log_BPR_23-05-2022_tagged.txt", "r") as f:
    data = f.read()
    reg_str = "<searchlog>(.*?)<searchlog/>"
    res = re.findall(reg_str, data, re.S)
    print(res[0])
    print(len(res))
    refine_res = [r.replace("\n","") for r in res]
    print(refine_res)
    for r in res:
        print(r.replace("\n",""))
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

print(refine_res)

exp = [":","=","--->",",","|"]
my_dict = {}
for result in refine_res:
    for char in result:
        if char in exp:
            key = result.split(char)[0]
            val = result.split(char)[1]
            my_dict[key] = val

print(my_dict)


import pandas as pd

data_df = pd.DataFrame({'key' : my_dict.keys() , 'value' : my_dict.values() })

data_df.head()