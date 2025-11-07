a = sorted([int(x) for x in input("Введіть числа через пробіл (від 1 до 1000): ")
            .split() if x.lstrip('-').isdigit() and 1 <= abs(int(x)) <= 1000])
if not a:
    print("Некоректні або порожні дані.")
else:
    t = int(input("Введіть число, яке потрібно знайти (1–1000): "))
    print(f"\nВідсортований список: {a}\n")
    l, r, s = 0, len(a) - 1, 1
    while l <= r:
        m = (l + r) // 2
        print(f"Крок {s}: [{l}..{r}], середній = {m}, значення = {a[m]}")
        if a[m] == t:
            print(f"\nЧисло {t} знайдено на позиції {m + 1}!")
            break
        l, r = (m + 1, r) if a[m] < t else (l, m - 1)
        s += 1
    else:
        print(f"\nЧисло {t} не знайдено у списку.")

