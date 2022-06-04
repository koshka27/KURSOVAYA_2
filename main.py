import json

import flask
from flask import Flask, jsonify
import utils
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(stream=open("api.log", "a"))
handler.setFormatter(logging.Formatter(fmt='%(asctime)s [%(levelname)s] %(message)s'))
logger.addHandler(handler)

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    logger.info("Запрос /")
    return flask.render_template("index.html", data=utils.get_posts_all())


@app.route("/posts/<postid>")
def get_post(postid):
    try:
        return flask.render_template("post.html", data=utils.get_comments_by_post_id(post_id=postid),
                                     data_from_main=utils.get_post_by_pk(postid))
    except ValueError:
        return "Ошиибка сервера!", 500

@app.route("/search/")
def search():
    search_string = flask.request.args.get("s")
    print(search_string)

    return flask.render_template("search.html", data=utils.search_for_posts(search_string))


@app.route("/users/<username>")
def user(username):
    return flask.render_template("user-feed.html", data=utils.get_posts_by_user(username))


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена!"


@app.route("/api/posts")
def posts():
    return app.response_class(
        response=json.dumps(utils.get_posts_all(), ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )


@app.route("/api/posts/<post_id>/")
def post_id_search(post_id):
    return app.response_class(
        response=json.dumps(utils.get_post_by_pk(post_id), ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(port=8080, debug=True)
