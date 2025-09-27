#4장 연습 10번
#알파벳 소분자아 숫자중 3글자를 랜덤으로 선택하여 패스워드를 생성

import random

a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 'v', 'u', 't', 'w', 'y', 'z', 'x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
pass1 = random.choice(a_list)
pass2 = random.choice(a_list)
pass3 = random.choice(a_list)

print(f"패스워드: {pass1}{pass2}{pass3}")
