from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #taking  home.html file from templates folder
    return render_template('home.html')

@app.route('/about')
def about():
    #about_me file from templates
    return render_template('about_me.html')

@app.route('/projects')
def projects():
    #projects file from templates
    return render_template('projects.html')

if __name__ == '__main__':
    # debug=True means the site updates instantly when I save changes
    app.run(debug=True)