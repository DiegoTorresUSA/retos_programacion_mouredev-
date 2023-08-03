""" EL FAMOSO "FIZZ BUZZ"
 * Fecha publicación enunciado: 27/12/21
 * Fecha publicación resolución: 03/01/22
 * Dificultad: FÁCIL
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con
 un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".



def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i, "Fizz")
        if i % 5 == 00:
            print(i, "Buzz")
        if i % 3 == 0 and i % 5 == 00:
            print(i, "fizzbuzz")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fizz_buzz()
"""


def fizz_buzzv2():
    divisible3 = [i for i in range(1, 101) if i % 3 == 0]
    divisible5 = [i for i in range(1, 101) if i % 5 == 0]
    divisible_ambos = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
    print(divisible3, "fizz")
    print(divisible5, "buzz")
    print(divisible_ambos, "fizzbuzz")


fizz_buzzv2()
