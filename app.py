from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog_1')
def blog_1():
    return render_template('imbracing-journey.html')

@app.route('/blog_2')
def blog_2():
    return render_template('finding-joy.html')

@app.route('/blog_3')
def blog_3():
    return render_template('how-coding.html')

@app.route('/blog_4')
def blog_4():
    return render_template('how-to.html')

@app.route('/blog_5')
def blog_5():
    return render_template('what-inspired.html')

@app.route('/blog_6')
def blog_6():
    return render_template('why-you.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)