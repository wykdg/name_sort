from functools import cmp_to_key
import json

data = json.load(open("./data.json", encoding="utf-8"))
word_dict = {}
for word, order in data:
    word_dict[word] = order

fuxing_set = set()
for line in open("fuxing.txt", encoding="utf-8"):
    fuxing = line.strip()
    fuxing_set.add(fuxing)


def split_name(x): #拆分姓名
    if x[:2] in fuxing_set:
        return x[:2], x[2:]
    else:
        return x[0], x[1:]


def compare_part_name(name1, name2):
    
    for c1, c2 in zip(name1, name2):
        if c1 == c2:
            continue
        bs1 = word_dict.get(c1,"66666")
        bs2 = word_dict.get(c2,"66666")
        bs1_len = len(bs1)
        bs2_len = len(bs2)
        if bs1_len != bs2_len:
            return bs1_len - bs2_len
        else:
            if bs1 < bs2:
                return -1
            elif bs1 > bs2:
                return 1
    if len(name1) != len(name2):
        return len(name1) - len(name2)
    return -1 if name1 < name2 else 1  # 实在比不了，字典序


def compare_name(name1, name2):
    surname1, personal1 = split_name(name1)
    surname2, personal2 = split_name(name2)

    if surname1 != surname2:
        return compare_part_name(surname1, surname2)

    if personal1 != personal2:
        return compare_part_name(personal1, personal2)

    return 0


names = open("names.txt", encoding="utf-8").readlines()
names = [n.strip() for n in names][::-1]

key = cmp_to_key(compare_name)
names.sort(key=key)
with open("out.txt","w",encoding="utf-8") as of:
    for name in names:
        of.write(name+"\n")