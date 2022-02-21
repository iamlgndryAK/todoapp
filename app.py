from flask import Flask, render_template, request, url_for, redirect

todo_list = []


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html", todo_list=todo_list)


@app.route("/show_list", methods=["POST", "GET"])
def show_list():
    new_task = request.form.get("title")
    if new_task not in todo_list:
        todo_list.append(new_task)
    print(todo_list)
    return redirect(url_for("home"))


@app.route("/delete/<int:index>", methods=["POST", "GET"])
def delete(index):
    todo_list.pop(index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)