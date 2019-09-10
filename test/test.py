import mod1      # 같은 경로상에 있는 mod1 모듈을 호출
print(mod1.add(2, 5))


from mod1 import add     # from mod1 import add, sub도 가능
print(add(2, 5))         # from mod1 import * 도 가능 (*은 모든 것이라는 뜻)


# if __name__ == "__main__"의 사용
# mod1.py에 print 실행문이 있을 때, test.py를 실행하면 mod1.py의 print문이 실행됨
# mod1.py에서 실행문에 if __name__ == "__main__"을 써주면 mod1.py에서 직접 실행했을 때는 __name__ == "__main__"이 참이 되어 if문이 실행됨
# test.py(다른 파일)에서 모듈을 불러서 사용할때는 __name__ == "__main__"이 거짓이 되어 실행이 안 됨


