from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


# @app.route("/")
# def hello_world0():
#     print(url_for('static', filename='chocolate_chip.ico'))
#     return render_template('index.html')



@app.route("/")
def my_home():
    
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data ["subject"]
        message = data ["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline = '', mode='a') as database2:
        email = data["email"]
        subject = data ["subject"]
        message = data ["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar='"' , quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return "form submitted hoooorayyy"
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # print(data)
            # write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'



# @app.route("/index.html")
# def index():
    
#     return render_template('index.html')


# @app.route("/works.html")
# def work():
    
#     return render_template('works.html')



# @app.route("/contact.html")
# def contact():
    
#     return render_template('contact.html')


# @app.route("/about.html")
# def about():
    
#     return render_template('about.html')


# @app.route("/components.html")
# def components():
    
#     return render_template('components.html')


# @app.route("/blog")
# def blog1():
#     return "<p>These are my thoughts <p>"




# @app.route("/1")
# def hello_world1():
#     return "<p>Hello, World aaaaaa!</p>"

# @app.route("/blog")
# def blog():
#     return "<p>These are my thoughts <p>"

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "<p>This is my dog <p>"

# # @app.route("/favicon.ico")
# # def ico():
# #     return "<p>chocolate_chip <p>"

if __name__== '__main__':
    app.run()