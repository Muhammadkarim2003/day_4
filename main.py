line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]

map = [line1, line2, line3]


pozitsiya = input("Koordinatni kiriting (masalan, a1, b2, c3): ")

letter = pozitsiya[0].lower()

abc = ["a", "b", "c"]
if letter not in abc:
    print("Noto'g'ri belgi kiritildi!")
    exit()

letter_index = abc.index(letter)
number_index = int(pozitsiya[1]) - 1
if number_index < 0 or number_index >= len(map):
    print("Noto'g'ri raqam kiritildi!")
    exit()

map[number_index][letter_index] = "X"

for line in map:
    print(' '.join(line))
