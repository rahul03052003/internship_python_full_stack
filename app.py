from flask import Flask,render_template

app=Flask(__name__)
#app.secret_key("hellothisissecret")

@app.route('/')
def indexpage():
    return render_template('index.html')  #pass the html file in it

@app.route('/createnewaccpage')
def createaccount():
    return render_template('createnewaccpage.html')

@app.route('/loginpage')
def loginpage():
    return render_template('loginpage.html')

if __name__=='__main__':
    app.run(debug=True)

