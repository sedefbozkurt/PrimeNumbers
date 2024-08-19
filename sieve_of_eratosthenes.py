def sieveOfEratosthenes(start, end):
    if start < 2:
        start = 2

    # Asal sayıları saklamak için bir liste
    primeList = []
    # 0'dan end değerine kadar olan tüm sayıların başlangıçta asal olduklarını varsay
    isPrime = [True for _ in range(end + 1)]
    p = 2

    while p ** 2 <= end:
        if isPrime[p]:
            # p'nin katı olan sayılar asal değildir ve false olarak işaretlenir
            for i in range(p ** 2, end + 1, p):
                isPrime[i] = False
        p += 1

    for num in range(start, end + 1):
        if isPrime[num]:
            primeList.append(num)

    return primeList

def main():
    while True:
        startInput = input("Başlangıç sayısını girin: ")
        endInput = input("Bitiş sayısını girin: ")

        if not startInput.isdigit() or not endInput.isdigit():
            print("Lütfen geçerli sayısal değerler giriniz!")
            continue

        start = int(startInput)
        end = int(endInput)

        if start >= end:
            print("Lütfen geçerli bir başlangıç ve bitiş değeri giriniz. Bitiş sayısı başlangıç sayısından büyük olmalı!")
            continue

        primeList = sieveOfEratosthenes(start, end)
        
        if not primeList:
            print(f"{start} ile {end} arasında asal sayı bulunmamaktadır.")
        else:
            print(f"{start} ile {end} arasındaki asal sayılar: {primeList}")

if __name__ == "__main__":
    main()