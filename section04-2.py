# Sction04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am boy"
str2 = 'NiceMan'
str3 = ''
str4 = str('')

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collenction\""
print(escape_str1)
escape_str2 = "Tap \t Tap \t"
print(escape_str2)

# Raw String 
raw_s1 = r'C:\Prgrams\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)



# 멀티라인
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc '
str_o3 = "def"
str_o4 = "NiceMan"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_o4) # a 라는 문자가 str_o4 에 포함되어 있냐? true false
print('z' not in str_o4)

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

b1 = 10.4
print(str(b1))

# 문자열 함수

# a = 'niceman'
# b = 'orange'

# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice', 'good'))
# print(list(reversed(b)))

# 인덱싱
# a = niceman -> n i c e m a n = size 7
a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1]) 


