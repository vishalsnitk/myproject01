from flask import Flask, render_template
#flask: here flask is our module and from there we import the Flask class.
# render_template: use to run html code


app = Flask(__name__)
#Flask(__name__): once flask application created we need to give it name   .... here name is refering to main     #
# print(__name__)               #it will print the main

#Any site will be having some url so when certain url is requested what it should return that we need to say to the flask
JOBS= [
  {
    "id":1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
  },
  {
    "id":2,
    "title": "SDE",
    "location": "Pune",
    "salary": "Rs. 14,00,000"
    
  },
  {
    "id":3,
    "title": "Influencer",
    "location": "Mumbai",
    "salary": "Rs. 14,00,000,0000"

  }
]

@app.route("/")  #way to perfrom the routing "/"
def hello_world():
  return render_template('home.html',jobs= JOBS)
  
#Data: data is send from list to html

#This is just way to run the flask application
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)   #0.0.0.0 to run locally
