s = input()
t = input()
mask = "abcdefghijklmnopqrstuvwxyz"
need_tree = array = automaton = False
for i in range(26):
    cs = s.count(mask[i])
    ct = t.count(mask[i])
    if ct < cs:
        automaton = True
    elif ct > cs:
        need_tree = True

index_found, match = 0, -1
for i in range(len(t)):
    index_found = s.find(t[i], match + 1)
    if index_found > match:
        match = index_found
    else:
        array = True
        break
if need_tree:
    print("need tree")
elif (automaton and array):
    print("both")
elif automaton:
    print("automaton")
elif array:
    print("array")


