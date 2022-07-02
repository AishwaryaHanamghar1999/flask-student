from flask import Flask, jsonify, render_template,url_for,json,request,redirect
from flask_mongoengine import MongoEngine
# from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['MONGODB_SETTINGS']={
    "db":"studentcrud",
    "host":"localhost",
    "port":27017
}
db=MongoEngine()
db.init_app(app)

class Student(db.Document):
    name=db.StringField()
    email=db.StringField()
    password=db.StringField()
    gender=db.StringField()
    age=db.IntField()
    
    def to_json(self):
        return {
            "name":self.name,
            "email":self.email,
            "password":self.password,
            "gender":self.gender,
            "age":self.age
        }

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add():
   if request.method=='POST':
       name=request.form['name']
       email=request.form['email']
       password=request.form['password']
       gender=request.form['gender']
       age=request.form['age']
    #    stu=User(name=name,email=email,password=password,gender=gender,age=age)
    #    stu.save()
    #    stud=User.find()
    #    return render_template('index.html',stud=stud)
       db.user.insert_one({'name':name,'email':email,'password':password,'gender':gender,'age':age})
       return redirect(url_for('home'))
#    stud=db.User.find()
   return render_template('index.html')
        


if __name__=="__main__":
    app.run(debug=True)