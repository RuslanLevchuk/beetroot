list = ['ibm', 'sony', 'ati', 'intel', 'amd', 'hp', 'panasonic']

print([str(n)+' '+str(v) for n, v in enumerate(list) if len(v)<=3])
print([str(n)+' '+str(v) for n, v in enumerate([i for i in list if len(i)<=3])])

"""два варіанти,відфільтровування по довжині: по переднній нумерації а також нумерація після фільтрування"""