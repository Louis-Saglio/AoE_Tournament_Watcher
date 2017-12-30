import flask
import graphic
import os
import data_getter

app = flask.Flask("AoE_Meme_Tournament")


@app.route("/")
def home():
    graphic.main(show=False)
    return flask.render_template("image.html")


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    os.system("python data_getter.py&")
    app.run(host='0.0.0.0', port=port)
