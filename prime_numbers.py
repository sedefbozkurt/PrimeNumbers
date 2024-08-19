"""
belirli bir aralıktaki asal sayıları kullanarak toplamları 34 olan farklı asal sayı üçlülerini bulur 
ve bu üçlüleri sayar. 
"""

def isPrime(number):
    """sayının asal olup olmadığını kontrol eder."""
    if number < 2:
        return False
    if number == 2:
        return True # 2 asal bir sayı
    if number % 2 == 0:
        return False # Diğer asal sayılar çift olamaz
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Önceden hesaplanmış asal sayılar listesi
primeNumbers = [x for x in range(2, 35) if isPrime(x)]

counter = 0
seenCombinations = set()

for x in primeNumbers:
    for y in primeNumbers:
        if y > x:
            z = 34 - x - y
            if z > y and isPrime(z):
                combination = tuple(sorted([x, y, z]))
                if combination not in seenCombinations:
                    seenCombinations.add(combination)
                    counter += 1
                    print(f"{x}, {y}, {z}")

print(f"Farklı üçlü sayısı: {counter}")