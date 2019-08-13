import os
import sys

names = []
with open("./data/names.txt") as f:
    for line in f:
        line = line.strip()
        fs = line.split("、")
        for w in fs:
            if len(w) > 3:
                continue
            names.append(w)

print(names)

ws_mid = {}
ws_last = {}
for w in names:
    if len(w) == 2:
        tk = w[1]
        if tk in ws_last:
            ws_last[tk] += 1
        else:
            ws_last[tk] = 1
    if len(w) == 3:
        tk = w[1]
        if tk in ws_mid:
            ws_mid[tk] += 1
        else:
            ws_mid[tk] = 1

        tk = w[2]
        if tk in ws_last:
            ws_last[tk] += 1
        else:
            ws_last[tk] = 1


print(ws_mid, ws_last)
