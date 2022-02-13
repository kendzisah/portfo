import datetime
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        date = date["date"]
        file = database.write(
            f'\n name: {name}, email: {email}, subject: {subject}, message: {message}, date: {date}')


def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        date = data["date"]
        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message, date])


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/<string:page>')
def return_page(page):
    return render_template(page)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            date = datetime.datetime.now()
            data["date"] = date.strftime("%x")
            print(data)
            # if data.get("name"):
            #     return redirect(f'/thankyou.html/{data.get("name")}')
            # else:
            #     return redirect(f'/thankyou.html')
            write_to_csv(data)
            return redirect(f'/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'Something went wrong'


# @app.route('/thankyou.html/<string:name>')
# def thank_you(name):
#     return render_template('./thankyou.html', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
