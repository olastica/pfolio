from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open("database.txt", mode='a') as database:
        database.write(f'\nEmail: {email}, Subject: {subject}, message: {message}')


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open("database.csv", newline='', mode='a') as database2:
        csv_writer = csv.writer('database.csv', delimiter=',', quotechar='"', quoting=csv.QUOTE.MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            feedback = "Thank you! I will get in touch with you shortly!"
            return render_template('/contact.html', message=feedback)
        except:
            return "Did not save data!"
    else:
        return "Something went wrong!"
