from flask import Flask, request, render_template

app = Flask(__name__)    # flask 객체 생성
@app.route('/index')          # 클라이언트에서 서버로 요청할 때 요청하는 주소값 (http://www.~.com/ 일 때 / 뒷부분이 요청하는 주소값)
def index():                  # 주소값(http://127.0.0.1:5000/)뒤에 index 입력하면 index 함수가 실행됨
    return 'Hello world!'

@app.route('/')  
def home():
    return render_template('home.html')

if __name__ == '__main__':          # 파일 내에서 호출하면 __main__
    app.run(debug=True, port=80)    # import해서 호출하면 파일명(__name__)
  # debug=True -> html문서 등의 내용들이 바뀔 때 알아서 인지
  # port=80 -> port번호를 변경하고자 하는 경우 입력


# app.py와 같은 위치에 templates폴더, teplates폴더 안에 html문서