# 주민등록번호 마지막 네 자리 가리는 프로그램 짜기

def mask_security_number(security_number):
    scr_num = str(security_number)
    masking = scr_num[:-4]
    return masking + '****'


# 테스트
print(mask_security_number("8803028475737"))
print(mask_security_number("981204-3827746"))
