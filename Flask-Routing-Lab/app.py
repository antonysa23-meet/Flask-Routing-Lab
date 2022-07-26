from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/shirt')
def shirt():
    return render_template('product_shirt.html')


@app.route('/jeans')
def jeans():
    return render_template('product_jeans.html')


@app.route('/heels')
def heels():
    return render_template('product_heels.html')


@app.route('/hat')
def hat():
    return render_template('product_hat.html')


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
