from flask import Flask  #here flask is our module and from there we import the Flask class.

app = Flask(__name__)
#once flask application created we need to give it name   .... here name is refering to main     #
# print(__name__)               #it will print the main

#Any site will be having some url so when certain url is requested what it should return that we need to say to the flask


@app.route("/")  #way to perfrom the routing "/"
def hello_world():
  return "<p>Hello, World!</p>"


#This is just way to run the flask application
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)   #0.0.0.0 to run locally
