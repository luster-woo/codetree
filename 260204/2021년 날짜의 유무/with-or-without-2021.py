m, D = map(int, input().split())

if m < 1 or m > 12:
    print("No")
elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print("Yes" if 1 <= D <= 31 else "No")
elif m == 4 or m == 6 or m == 9 or m == 11:
    print("Yes" if 1 <= D <= 30 else "No")
else:  # m == 2
    print("Yes" if 1 <= D <= 28 else "No")
