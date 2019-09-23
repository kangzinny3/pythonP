from flask import Flask, render_template, request, redirect, url_for
import mariadbfunc as db

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('homeblock.html')

@app.route('/formtest')
def formtest():
    return render_template('formtestblock.html')

# db와 연동
@app.route('/insertbook', methods=['POST'])
def insertbook():
    data = (request.form['title'], request.form['date'], request.form['publisher'], request.form['pages'], request.form['recommend'])
    db.create_table()
    db.insert_books(data)
    return redirect(url_for('booklist'))
    # route를 호출하지 못하는 경우 함수를 직접적으로 호출할 때 url_for(함수이름) 사용

@app.route('/booklist')
def booklist():
    books = db.all_books()
    print(books)
    return render_template('booklist.html', books = books)
                                            # books를 booklist.html에 books라는 이름으로 넘겨줌

@app.route('/content/<title>')
def content(title):         # 꼭 매개변수(여기서는 title) 값 전달받아야 함
    book = db.where_book(title)
    return render_template('content.html', book = book)

if __name__ == '__main__':
    app.run(debug=True,port=80)
