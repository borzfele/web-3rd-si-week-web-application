from flask import Flask, request, render_template, redirect, url_for
import psycopg2
import sql_queries


app = Flask(__name__)


@app.route('/')
def main_menu():
    return render_template('index.html')

@app.route('/mentors')
def list_mentors():
    return render_template('list.html', mentors_and_schools=sql_queries.mentors_and_schools())


@app.route('/all-schools')
def all_schools():
    return render_template('list.html', all_schools=sql_queries.all_schools())


@app.route('/mentors-by-country')
def mentors_by_country():
    return render_template('list.html', mentors_by_country=sql_queries.mentors_by_country())


@app.route('/contacts')
def contacts():
    return render_template('list.html', contacts=sql_queries.contacts())


@app.route('/applicants')
def applicants():
    return render_template('list.html', applicants=sql_queries.applicants())


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    return render_template('list.html', applicants_and_mentors=sql_queries.applicants_and_mentors())


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
