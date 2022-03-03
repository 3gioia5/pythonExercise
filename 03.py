# 원화 -> 달러, 원화 -> 엔화 환전 함수 만들기

def krw_to_usd(krw):
    return krw / 1000

def usd_to_jpy(usd):
    return usd / 8 * 1000

prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: ", prices)

i = 0
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1

print("미국 화폐: ", str(prices))

i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1

print("일본 화폐: ", str(prices))
