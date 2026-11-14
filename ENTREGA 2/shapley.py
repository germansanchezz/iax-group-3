#!/usr/bin/env python3
"""
Valor de Shapley con la fórmula:
  phi_i = sum_{S ⊆ N\\{i}} |S|!(n-|S|-1)!/n! * [v(S∪{i}) - v(S)]

Uso:
  python shapley.py
  python shapley.py 3 0 1 1 2 1 2 2 3
  python shapley.py 3 -f "x1 + 2*x2 + 3*x3"

v(S) se introduce en orden de máscara binaria:
  0=∅, 1={1}, 2={2}, 3={1,2}, 4={3}, ...
"""

import sys
from fractions import Fraction
from math import factorial


def nombre(S, n):
    js = [str(j + 1) for j in range(n) if S >> j & 1]
    return "{" + ",".join(js) + "}" if js else "∅"


def desde_funcion(n, f):
    """Vector v(S) a partir de f(S), con S un set de jugadores, p. ej. {1,2}."""
    return [Fraction(f({j + 1 for j in range(n) if S >> j & 1})) for S in range(2 ** n)]


def shapley(n, v):
    tablas, phi = [], []
    for i in range(n):
        filas, total = [], Fraction(0)
        for S in range(2 ** n):
            if S >> i & 1:
                continue
            k = bin(S).count("1")
            w = Fraction(factorial(k) * factorial(n - k - 1), factorial(n))
            m = v[S | 1 << i] - v[S]
            filas.append((nombre(S, n), k, v[S | 1 << i], v[S], m, w, w * m))
            total += w * m
        tablas.append(filas)
        phi.append(total)
    return tablas, phi


def imprimir(cabeceras, filas):
    filas = [cabeceras] + [list(f) for f in filas]
    ancho = [max(len(str(f[j])) for f in filas) for j in range(len(cabeceras))]
    for f in filas:
        print("  ".join(str(x).ljust(a) for x, a in zip(f, ancho)))


def mostrar_orden(n):
    print("Orden:", ", ".join(f"{S}={nombre(S, n)}" for S in range(2 ** n)))


AYUDA = """\
Uso:
  python shapley.py                       modo interactivo
  python shapley.py n v0 v1 ...           vector de valores v(S)
  python shapley.py n -f "expresion"      función en x1,...,xn
  python shapley.py -h                    muestra esta ayuda

El vector v(S) contiene los 2^n valores en orden de máscara binaria:
  0=∅, 1={1}, 2={2}, 3={1,2}, 4={3}, 5={1,3}, ...
El bit j-1 de la máscara indica si el jugador j está en S.

En modo función, xj vale 1 si el jugador j está en S y 0 si no.
Usa * para multiplicar y ** para potenciar (^ no es potencia en Python).

Salida: una tabla por jugador con S, |S|, v(S∪{i}), v(S), contribución
marginal, peso y aporte, más un resumen con la comprobación de eficiencia.

Ejemplos:
  python shapley.py 3 0 1 1 2 1 2 2 3
  python shapley.py 3 -f "x1 + 2*x2 + 3*x3"
  python shapley.py 5 -f "x1 + x3 + 2*x4 + 3*x1*x2 + 5*x2*x5 - 10*x1*x2*x4"
"""


def main():
    args = sys.argv[1:]
    if args and args[0] in ("-h", "--help"):
        print(AYUDA)
        return

    n = int(args[0]) if args else int(input("n: "))
    assert n >= 1, "n debe ser >= 1."
    mostrar_orden(n)

    if args and len(args) > 1 and args[1] in ("-f", "--func"):
        expr = " ".join(args[2:])

        def f(S):
            return eval(expr, {"__builtins__": {}},
                        {f"x{j}": int(j in S) for j in range(1, n + 1)})

        v = desde_funcion(n, f)
    elif args:
        v = [Fraction(x) for x in args[1:]]
    else:
        v = [Fraction(x) for x in input("v(S): ").replace(",", " ").split()]

    assert len(v) == 2 ** n, f"Se esperaban {2 ** n} valores y hay {len(v)}."
    tablas, phi = shapley(n, v)

    for i, filas in enumerate(tablas):
        print(f"\nJUGADOR {i + 1}")
        imprimir(["S", "|S|", f"v(S∪{{{i + 1}}})", "v(S)", "marginal", "peso", "aporte"], filas)
        print(f"phi_{i + 1} = {phi[i]}")

    print("\nRESUMEN")
    imprimir(["Jugador", "phi_i"], [[i + 1, phi[i]] for i in range(n)])
    suma = sum(phi)
    print(f"Suma = {suma}   v(N) = {v[-1]}   ->", "OK" if suma == v[-1] else "ERROR")


if __name__ == "__main__":
    main()
