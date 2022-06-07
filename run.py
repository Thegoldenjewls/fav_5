from flask import Flask

app = Flask(__name__)

@app.route("1")
def home():
    return "<h1>Home/Index</h1>"

    @app.route("2")
def fav5():
    return "<p1>My Favorite Sports Figures</h1>"
    player_dict = {
        '1': 'Kobe Bryant'
        '2': 'Cristiano Ronaldo'
        '3' : 'Michael Jordan'
        '4' : 'Leo Messi'
        '5' : 'Zlatan Ibrahimovic'
          }
