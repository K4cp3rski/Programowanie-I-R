choice = int(input("Jaką operację chcesz wykonać?\n(1-bit shift w prawo, 2-bit shift w lewo, "
                   "3-bitowa negacja "
                   # "4-bitowa alternatywa, 5-bitowa koniunkcja"
                   ")\n"))
var = int(input("Jaką liczbę chcesz poddać operacji?\n"))

if choice == 1:
    n = int(input("O ile bitów w prawo?\n"))
    out = int(bin(var >> n)[2:], 2)
elif choice == 2:
    n = int(input("O ile bitów w lewo?\n"))
    out = int(bin(var << n)[2:], 2)
elif choice == 3:
    print("Negacja")
    if var >= 0:
        out = -int(bin(~var)[3:], 2)
    else:
        out = int(bin(~var)[2:], 2)
# elif choice == 4:
#     n = int(input("Z jaką liczbą zrobić alternatywę?\n"))
#     out = int(bin(var & n)[2:], 2)
# elif choice == 5:
#     n = int(input("Z jaką liczbą wziąć koniunkcję?"))
#     out = int(bin(var | n)[2:], 2)
else:
    out = "Proszę wpisać właściwą wartość"

print(out)
