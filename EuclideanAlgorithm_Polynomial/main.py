import sympy

# 多項式の変数を定義
x = sympy.symbols("x")

# 与えられた多項式を定義
phi = x**7 + 2 * x**6 + x**5 + 3 * x**4 + 3 * x**3 + 2 * x**2 + x + 2
psi = x**5 - 1

# ユークリッドの互除法の計算
while psi != 0:
    quotient, remainder = sympy.div(phi, psi)
    print("phi:", phi)
    print("psi:", psi)
    print("quotient:", quotient)
    print("remainder:", remainder)
    print()
    phi = psi
    psi = remainder

gcd = phi
print("f(x) =", gcd)
