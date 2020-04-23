# personal-website

To create a virtual environment
'''
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
'''

To run the code
'''
python manage.py runserver
'''

To test the email server. The email server is configured in mysite/settings.py
'''
python -m smtpd -n -c DebuggingServer localhost:1025
'''