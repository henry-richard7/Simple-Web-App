from flask import Flask, render_template, request
from tmdbv3api import TMDb, Movie
from flask_paginate import Pagination, get_page_parameter

tmdb = TMDb()
tmdb.api_key = '' #Replace with your API Key

tmdb.language = 'en'

movie = Movie()

app = Flask(__name__, static_url_path='/static')


@app.route('/Movies', methods=['GET'])
def popular():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    popular_movies = movie.popular(page)
    pagination = Pagination(page=page, total=450, css_framework="bootstrap4")
    return render_template('Movies.html', Movies=popular_movies, pagination=pagination)


@app.route('/Movie_Detail', methods=['GET'])
def details():
    movie_id = request.args.get('id')
    m = movie.details(movie_id)
    crews = movie.credits(movie_id)

    if len(movie.videos(movie_id)) != 0:
        return render_template('Movies_Details.html', Movies=m, Crews=crews,
                               youtube=movie.videos(movie_id)[0].get("key"))
    else:
        return render_template('Movies_Details.html', Movies=m, Crews=crews,
                               youtube="")


@app.route('/Search', methods=['GET'])
def search():
    query = request.args.get('query')
    searching = movie.search(query)
    return render_template('search.html', Movies=searching)


if __name__ == '__main__':
    app.run(debug=True)
