def reverse(st):
    if type(st) == str:
        st = st.split()
    if len(st) == 1:
        return st[0]
    else:
        return st.pop()+' '+reverse(st)



assert reverse('магистр Йода так говорит поскольку джедай') == 'джедай поскольку говорит так Йода магистр'
