from flask import Flask, request, send_file, url_for, render_template, abort, redirect


app = Flask(__name__)

# @app.get("/users") #C
# @app.post("/users") #R
# @app.put("/user/{1}") #U
# @app.delete("/user/{1}") #D


test_name = "Menu"
menu = [
    {"pizza": "Пеперони", "ingredients": "Перетертые томаты, моцарелла, салями пикантные пепперони. Аллергены: злаки, лактоза.", "price": 305},
    {"pizza": "Сырная", "ingredients": "Моцарелла беби, фета, пармезан, горгонзола, проволоне, моцарелла. Аллергены: глютен, лактоза.", "price": 280},
    {"pizza": "Маргарита", "ingredients": "Перетертые томаты, моцарелла, базилик. Аллергены: злаки, лактоза.", "price": 190}
]


@app.get("/results/")
def results():
    context = {
        "Title": "ODERMAN",
        "menu": menu,
        "test_name": test_name
    }
    return render_template("results.html", **context)


@app.get("/")
def index():
    return render_template("index3.html",
                           Title="Victor",
                           info="I learn Djinja")


#Эта часть не относиться к дз
@app.post("/login/")
def login():
    user = request.form["name"]
    if user == "admin":
        return "Hello Admin"
    else:
        return redirect(url_for("login"), code=302)

@app.get("/login/")
def get_login():
    return render_template("login.html")


@app.errorhandler(404)
def page_not_found(error):
    return "Page not found my darling", 404


if __name__ == '__main__':
    app.run(port=5050, debug=True)
