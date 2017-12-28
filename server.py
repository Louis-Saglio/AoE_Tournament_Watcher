import flask

app = flask.Flask("AoE_Meme_Tournament")


@app.route("/")
def home():
    return flask.render_template("image.html")
