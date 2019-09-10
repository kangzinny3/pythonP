def add(a, b):
    return a + b

def sub(a, b):
    return a - b


if __name__ == "__main__":      
    print(add(1, 4))
    print(sub(4, 2))
# mod1.py에서 직접 실행할 때는__name__ 변수에 __main__ 값이 저장됨
# test.py(다른 파일)에서 실행할 때는 __name__ 변수에 mod1.py의 모듈 이름 값 mod1이 저장됨

