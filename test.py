def primes(number):
    if isinstance(number, int) == False:
        print("This is not an integer, please set another number!")
        return
    if number > 1:
        for i in range(2,number):
                if (number % i) == 0:
                    print("Number " + str(number) + " is a prime number")
                else:
                     print("Number " + str(number) + " is not a prime number")
                break
    else:
        print(str(number) + " is not a prime number")

primes(555)

# w domu
# weź tekst z jakiegoś artykułu, wrzuć do pliku txt, potem zrób kod, który wyczyści przecinki, kropki itd
