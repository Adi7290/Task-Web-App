from flask import Flask,render_template
app = Flask('__name__')

@app.route('/index.html')

def index():
    return render_template("/index.html")

@app.route('/add.html')

def add():
    return render_template("/add.html")

@app.route('/save.html')
def save():
    return render_template("/save.html")



if __name__=="__main__":
    app.run(debug=True,port=8000)