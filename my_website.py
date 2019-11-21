from flask import Flask,render_template

app=Flask(__name__)


@app.route('/forest_fires_table/')
def forest_fires_table():
  return render_template("forest_fires_table.html")

@app.route('/Forest_fires/')
def Forest_fires():
  return render_template("Forest_fires.html")

@app.route('/description/')
def description():
  return render_template("description.html")

@app.route('/')
def home():
  return render_template("home.html")

if __name__=="__main__":
  app.run(debug=True)
