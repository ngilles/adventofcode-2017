
# Inverse captcha

def captcha1(s):
    l = len(s)
    return sum(int(s[i]) for i in range(l) if s[i] == s[(i+1)%l])

def captcha2(s):
    l = len(s)
    return sum(int(s[i]) for i in range(l) if s[i] == s[(i+l/2)%l])

data = open('input.txt', 'r').read()

assert captcha1('1122') == 3
assert captcha1('1111') == 4
assert captcha1('1234') == 0
assert captcha1('91212129') == 9

print(captcha1(data))

assert captcha2('1212') == 6
assert captcha2('1221') == 0
assert captcha2('123425') == 4
assert captcha2('123123') == 12
assert captcha2('12131415') == 4

print(captcha2(data))
