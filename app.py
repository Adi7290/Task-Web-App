from flask import Flask,render_template,request,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Tasks(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)-> str:
        return f"{self.username}-{self.description}"




class Queries(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(20),nullable=False)
    message = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)-> str:
        return f"{self.name}-{self.email}-{self.subject}-{self.message}"
        


@app.route('/')
def home():
    return render_template('index.html',title="Homepage")

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        username = request.form['username']
        description = request.form['description']
        task = Tasks(username=username, description = description)
        db.session.add(task)
        db.session.commit()
        return redirect('/tasks')
    return render_template('Add.html',title='Add Task')

@app.route('/tasks')
def tasks():
    alltasks = Tasks.query.all()
    return render_template('tasks.html',title='Your Tasks',alltasks=alltasks)

@app.route('/delete/<int:sno>')
def delete(sno):
    task = Tasks.query.filter_by(sno=sno).first()
    db.session.delete(task)
    db.session.commit()
    return redirect('/tasks')



@app.route('/email',methods=['GET','POST'])
def email():
    if request.method=='POST':
        name = request.form['name']
        email= request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        query = Queries(name = name , email= email,subject=subject,message=subject)
        db.session.add(query)
        db.session.commit()
    return render_template('email.html',title='Email Us')

@app.route('/chat')
def chat():
    return render_template('chat.html',title='Chat with Us')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html',title='Give Feedback')





if __name__=="__main__":
    app.run(debug=True,port=8000)
