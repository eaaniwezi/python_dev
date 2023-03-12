from flaskblog import app, db

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()


# https://flask.palletsprojects.com/en/2.2.x/quickstart/
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
