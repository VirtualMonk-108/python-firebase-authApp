import pyrebase
from flask import *
app = Flask(__name__)

config = {

}

firebase = pyrebase.initialize_app(config)


@app.route('/', methods=['GET', 'POST'])



auth = firebase.auth()

#email = input('Please enter your username and password\n')
#password = input('Please enter your password\n')

#user = auth.create_user_with_email_and_password(email, password)
#user = auth.sign_in_with_email_and_password(email, password)
#auth.send_email_verification(user['idToken'])
#auth.send_password_reset_email(email)

#print(auth.get_account_info(user['idToken']))
