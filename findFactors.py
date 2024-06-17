def findFactors(number):
    # Negatif veya sıfır kontrolü
    if number <= 0:
        raise ValueError("Lütfen pozitif bir tam sayı giriniz.")

    # Benzersiz bölenleri tutmak için set oluştur
    factors = set()

    # 1'den sayının kareköküne kadar olan sayıları kontrol et
    # bir sayının bölenleri karekökünün iki tarafında simetrik olarak bulunur.
    for i in range(1, int(number ** 0.5) + 1):
        # i, sayıyı kalansız bölüyorsa
        if number % i == 0:
            # i sayısını bölenler setine ekle
            factors.add(i)
            # kullanıcının girdiği sayının diğer böleni
            factors.add(number // i)

    # seti sıralı bir liste olarak döndür
    return sorted(factors)

if __name__ == "__main__":
    try:
        num = int(input("Tam bölenlerini buldurmak istediğiniz sayıyı giriniz: "))
        divisors = findFactors(num)
        print(f"{num} sayısının tam bölenleri {divisors}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Hata oluştu: {e}")