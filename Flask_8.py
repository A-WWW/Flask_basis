from flask import Flask, render_template, url_for



app = Flask(__name__)
menu = ["Тестирование", "Отработка шаблона", "Проверка передачи"]

# "/" URL адресс, в данном случае главная страница
@app.route("/Eighth") #привязка функции к адрессу
@app.route("/") # url_for возращает только ближайший к функции
def index():
    print(url_for("index"))
    return render_template("framework.html", title="V_8.4", menu=menu)

@app.route("/test")
def test():
    print(url_for("test"))
    return render_template("test.html", menu=menu)

@app.route("/test_1/<path:username>")#динамический
def test_1(username):
    return f"Владелец:{username}"


#еще одна страница
@app.route("/base")
def base():
    print(url_for("base"))
    return render_template("base.html", title="Base V_1.4")

#тест без запуска сервера
#with app.test_request_context():
     #print(url_for("index"))
     #print(url_for("test"))
     #print(url_for("base"))

#только для локального сервера
if __name__ == "__main__":
    app.run(debug=True)
