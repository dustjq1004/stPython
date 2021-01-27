# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력 - 변수, 문자열, 숫자
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black paradise', end=' ')
print('piano notes')

print()

#format 사용 [], {}, ()
print('{} and {}'.format('You', 'me'))
print("{0} and {1} and {0}".format('You', 'Me')) #--> {} 안에 숫자를 넣으면 인덱스가 됨
print("{a} are {b}".format(a='You', b='Me')) # --> 좀 더 직관적임

print("%s's favorite number is %d" % ('Eunki', 7)) #%s: 문자, %d : 정수, %f : 실수

print("Test1: %5d, Price: %4.2f" % (776, 6534.12))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.12))

print()

print('\'you\'')
print("'you'")
print('"you"')
print("""'you'""")
print('\\you\\\n\n\n\n\n')
print('\t\t\ttest')

