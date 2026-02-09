from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)
Base = declarative_base()

class User(base):
  __tablename__ = "users"

  id = = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"<User(id={self.id}, name={self.name})>"
@app.route("/")
def index():
