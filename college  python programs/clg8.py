name = ['hi','hello','python','demo']
ilen = []
for a in name:
    ilen.append(len(a))
print('correct word:',name[ilen.index(max(ilen))])
