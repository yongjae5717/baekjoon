import sys

score = int(sys.stdin.readline())
if score > 89:
    print("A")
elif 79 < score < 90:
    print("B")
elif 69 < score < 80:
    print("C")
elif 59 < score < 70:
    print("D")
else:
    print("F")