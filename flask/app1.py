from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/user/<username>')
# def show_username(username):
#     return 'Username : %s' % username

# @app.route('/user/<username>/<int:age>') 
# def show_user_profile(username, age): 
#     return 'Username : %s, 나이 : %d' % (username, age) 

@app.route('/forminput')
def form_input():
    return render_template('form_input.html')

@app.route('/method/', methods=['GET', 'POST'])   # methods 안적으면 get이 기본
def login():                                      # /method 만 하고 /method/로 호출하면 Not Found
    if request.method == 'POST':                  # /method/ 하고 /method로 호출해도 자동으로 /method/로 호출됨
        name =  request.form['username'] 
        pwd = request.form['password']
        # return "Post %s, %s" % (name, pwd)
        
    else:
        name = request.args.get('username')     # form_input.html에서 input에서 name으로 지정해줘야함
        pwd = request.args.get('password')
        # return "Get %s, %s" % (name, pwd)
    return render_template('form_result.html', username=name, password=pwd)

if __name__ == '__main__':
    app.run(debug=True, port=80)

