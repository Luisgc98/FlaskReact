from flask import redirect, url_for
from app import create_app

app = create_app()

@app.route("/")
def index():

    return redirect(url_for('main.home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)