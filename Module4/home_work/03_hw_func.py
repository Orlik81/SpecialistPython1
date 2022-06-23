# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

x1 = float(input("Введите координаты x1= "))  # ax
y1 = float(input("Введите координаты y1= "))  # ay
x2 = float(input("Введите координаты x2= "))  # bx
y2 = float(input("Введите координаты y2= "))  # by
r1 = float(input("Введите r1 = "))
r2 = float(input("Введите r2= "))


def circle_in_circle(x1, y1, x2, y2, r1, r2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if d < (r1 - r2):
        return "yes"
    else:
        return "No"

print(circle_in_circle(x1, y1, x2, y2, r1, r2))
