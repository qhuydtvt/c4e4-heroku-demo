from flask import Flask, render_template
import mongoengine
from mongoengine import Document, StringField

host = "ds011893.mlab.com"
port = 11893
db_name = "c4e_rss"
user_name = "c4e"
password = "codethechange"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", movie_list = Movie.objects)

@app.route("/giang")
def hello_giang():
    return "Hello Giang"

@app.route("/<name>")
def hello(name):
    return "Hello " + name

# Render HTML file
@app.route("/test-render")
def test_render():
    return render_template("movie.html")

# Render HTML file with data
@app.route("/movie")
def movie():
    return render_template("movie_2.html",
                           title = "Civil war",
                           img="https://40.media.tumblr.com/be71c589139ae879bb0f7c0de4967ceb/tumblr_o4jm34bJLM1rlfwxeo1_540.jpg")


# Render HTML file with list of data

# class Movie:
#     def __init__(self, title, img):
#         self.title = title
#         self.img = img
#
# m1 = Movie(title="Kungfu panda", img="https://upload.wikimedia.org/wikipedia/en/e/e6/Kung_Fu_Panda_3_poster.jpg")
# m2 = Movie(title="Rush hour", img="http://ia.media-imdb.com/images/M/MV5BMjAyMzAyNzY5N15BMl5BanBnXkFtZTcwNjU3MTc0MQ@@._V1_SX640_SY720_.jpg")
# m3 = Movie(title="The social network", img="http://images.pcworld.com/news/graphics/206218-the_social_network_original.jpg")
# m_list = [m1, m2, m3]

class Movie(Document):
    title = StringField()
    img = StringField()

@app.route("/movies")
def get_movies():
    return render_template("movie_3.html", movie_list=Movie.objects)

# Now deploy to heroku

# Render template, load data from database
if __name__ == '__main__':
    app.run()
