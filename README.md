# Quarn Examinator
An app that exams your quarn memorization.\
However it is not listening to you, but it takes an exams from the number of the verse\
Which means a random verse will come up and you have to type in the correct verse number and surah.

## Screenshots:
![ScreenShot No.1](shots/1.png?raw=true "Screenshot No.1")
![ScreenShot No.2](shots/2.png?raw=true "Screenshot No.2")

## Usage:
1. Clone the project
2. Activate virtual Envirement
3. Run `pip3 install -r requirement.txt`
4. Run `python3 app.py` or `flask run`
5. Open the browser on localhost port `3333`

## Extra Info:
1. The website is in Arabic lanuguage.
2. You may see the website already has some verses saved, if you want delete them, just re-create the `db.sqlite3` and go to localhost:3333/migrate, after that you are good to go.

## Contirbuting:
Fell free to contirbute to this project as it is completely open source and free to use.\
I'm going to list a ***TODO*** for you in order to work on, if you are intersted.

## Project:
This project is made in flask with python3 and using SQLAlchemy to deal with databse.\
As the project is so small, there isn't much things to document about. and the code is self-explaintory.\
No other css or js framework are used corrently and the font's are free to use from google fonts.

## TODO:
1. Add the `Editing verse` feature, it is really important, also `Editing surah`
2. Create a good project structure, where every code is in it's own place and not all of them in the same `app.py` file.
3. Even Add more Verses to databse, (Help to complete the db)

