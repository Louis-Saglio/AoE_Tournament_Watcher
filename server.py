import flask
import graphic

app = flask.Flask("AoE_Meme_Tournament")
app.debug = True


@app.route("/")
def home():
    graphic.main(show=False)
    return flask.render_template("image.html")


if __name__ == '__main__':
    app.run(debug=True)
