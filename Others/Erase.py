n = int(input())
s1 = input()
s2 = input()
failed = False
if n % 2 != 0:
    for i in range(len(s1)):
        if (s1[i] == s2[i]):
            failed = True
            break
    if failed:
        print("Deletion failed")
    else:
        print("Deletion succeeded")
else:
    if s1 != s2:
        print("Deletion failed")
    else:
        print("Deletion succeeded")
