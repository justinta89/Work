from justin import app


LST = ["index", "blog"]
SOCIALLIST = ["facebook", "twitter", "linkedin", "github"]

@app.route('/index')
def index():
    return render_template('index.html', LST = LST, SOCIALLIST = SOCIALLIST)

@app.route('/blog')
def blog():
    return render_template('blog.html', LST = LST, SOCIALLIST = SOCIALLIST)


if __name__ in ['__console__', '__main__']:
    app.run(debug=True)