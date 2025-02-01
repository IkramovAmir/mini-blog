from flask import Flask, render_template, request

app = Flask(__name__)

blogs = [
    {"id": 1, "title": "Birinchi blog", "content": "Bu birinchi blog postining kontenti."},
    {"id": 2, "title": "Ikkinchi blog", "content": "Bu ikkinchi blog postining kontenti."},
    {"id": 3, "title": "Uchinchi blog", "content": "Bu uchinchi blog postining kontenti."}
]

@app.route("/")
def index():
    search_query = request.args.get("search")
    if search_query:
        filtered_blogs = [blog for blog in blogs if search_query.lower() in blog["title"].lower()]
    else:
        filtered_blogs = blogs
    return render_template("index.html", blogs=filtered_blogs)

@app.route("/blogs")
def all_blogs():
    return render_template("blogs.html", blogs=blogs)

@app.route("/blogs/<int:id>")
def blog_detail(id):
    blog = next((blog for blog in blogs if blog["id"] == id), None)
    if blog:
        return render_template("detail.html", blog=blog)
    return "Blog topilmadi", 404

@app.route("/add", methods=["GET", "POST"])
def add_blog():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_blog = {
            "id": len(blogs) + 1,
            "title": title,
            "content": content
        }
        blogs.append(new_blog)
        return render_template("add.html", success=True)
    return render_template("add.html", success=False)

@app.route("/delete/<int:id>")
def delete_blog(id):
    global blogs
    blogs = [blog for blog in blogs if blog["id"] != id]
    return render_template("blogs.html", blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)
