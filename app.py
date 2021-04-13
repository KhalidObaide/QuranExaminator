from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


# App configuration
app = Flask(__name__, template_folder="./templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

# Models
class Surah(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return self.name
class Verse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surah = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    verse = db.Column(db.String(4000), nullable=False)
    def __repr__(self):
        return self.verse


# Exam route
@app.route('/')
def index():
    return render_template('index.html')

# adding page
@app.route('/add')
def add():
    verses = Verse.query.all()
    all_surahs = Surah.query.all()
    last_surah = Surah.query.get(verses[-1].surah)
    surah_verses = []
    for surah in all_surahs:
        n_verses = []
        for verse in verses:
            if verse.surah == surah.id:
                n_verses.append(verse)
        surah_verses.append({
            "surah": surah.name, "verses": str(len(n_verses))
        })
    return render_template('add.html', all_surahs=all_surahs, last_surah=last_surah, surah_verses=surah_verses)


# Add surah form route
@app.route('/add_surah/', methods=['POST'])
def add_surah():
    number, name = request.form.get('number'), request.form.get('surah')
    if not number or not name:
        return "Please fill the required fields"
    surah = Surah()
    surah.number = int(number)
    surah.name = name
    db.session.add(surah)
    db.session.commit()
    return redirect('/add')

# Add verse form route
@app.route('/add_verse/', methods=['POST'])
def add_verse():
    verse, surah, number = request.form.get('verse'), request.form.get('surah'), request.form.get('number')
    if not verse or not surah or not number:
        return "Please fill the required fields"
    surah = Surah.query.filter_by(name=surah).first()
    if not surah:
        return "Wrong data inserted"
    number = int(number)
    n_verse = Verse()
    n_verse.surah = surah.id
    n_verse.number = number
    n_verse.verse = verse
    db.session.add(n_verse)
    db.session.commit()
    return redirect('/add')

# migrate route
@app.route('/migrate')
def migrate():
    db.create_all()
    return "Migrated"

# running the app
if __name__ == '__main__':
    app.run(debug=True, port=3333)
