import flask
import graphic

app = flask.Flask("AoE_Meme_Tournament")


@app.route("/")
def home():
    graphic.main(show=False)
    return flask.render_template("image.html")
