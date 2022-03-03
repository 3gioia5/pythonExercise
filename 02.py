# 화씨 온도 리스트를 섭씨 온도 리스트로 변환하기

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: ", temperature_list)

i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1

print("섭씨 온도 리스트: ", temperature_list)