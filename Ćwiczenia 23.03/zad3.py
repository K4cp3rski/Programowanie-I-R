import time

start = time.process_time()

opening = ['(', '{', '[']
ending = [')', '}', ']']

nitka1 = "{}(({{}}))[[(())]]"
nitka2 = "{{}](({{}}))[[(())]]"

def par_check (nitka):
    # print(nitka)
    stosik = []
    for i in nitka:
        if i in opening:
            stosik.append(i)
        elif i in ending:
            poz = ending.index(i)
            # print(poz)
            # print(i)
            if (len(stosik) >0) and (opening[poz] == stosik[len(stosik)-1]):
                stosik.pop()
            else:
                # print(stosik)
                return "niedopasowane"
    if len(stosik) == 0:
        # print(stosik)
        return "dopasowane"

print(f"Ciąg {nitka1} ma", par_check(nitka1),"nawiasy.")
print(f"Ciąg {nitka2} ma", par_check(nitka2),"nawiasy.")

duration = time.process_time() - start
print("{0:02f}s".format(duration))