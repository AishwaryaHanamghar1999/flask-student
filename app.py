from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///student.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Stud(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(50))
    password=db.Column(db.Integer)
    gender=db.Column(db.String(100))
    age=db.Column(db.Integer)
    
    def __init__(self,sno,name,email,password,gender,age):
        self.sno=sno
        self.name=name
        self.email=email
        self.password=password
        self.gender=gender
        self.age=age
        
    def __repr__(self) :
        return f"{self.id}:{self.name}"
            
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        gender=request.form['gender']
        age=request.form['age']
        stu=Stud(name=name,email=email,password=password,gender=gender,age=age)
        db.session.add(stu)
        db.session.commit()
    data=Stud.query.all()
    return render_template('index.html',data=data)

@app.route('/show')
def show():
    all=Stud.query.all()
    print(all)
    

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
   stu=Stud.query.filter_by(sno=sno).first()
   return render_template('update.html',stu=stu)

@app.route('/delete/<int:sno>')
def delete(sno):
    stu=Stud.query.filter_by(sno=sno).first()
    db.session.delete(stu)
    db.session.commit()
    return redirect('/')
    

if __name__=='__main__':
    app.run(debug=True)