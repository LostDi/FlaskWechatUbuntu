from flask import Flask;
from app import app;
from flask_sqlalchemy import SQLAlchemy;

#database
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:newhappy123pd-@localhost/test'
db=SQLAlchemy(app)

class BackData(db.Model):
    __tablename__='pet'
    id =db.Column('id',db.Integer,primary_key=True)
    situation=db.Column('situation',db.Unicode)
    name=db.Column('name',db.Unicode)
    
    def __init__(self,name,id,situation):
        self.id=id;
        self.name=name;
        self.situation=situation; 

    
    