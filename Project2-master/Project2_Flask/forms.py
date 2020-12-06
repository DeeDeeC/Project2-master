from Project2_Flask import app
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
import requests
from Project2_Flask import main_functions


class NewsForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    author = SelectField('Author', choices=[('Haruki Murakami', 'Haruki Murakami'),
                                            ('Yukio Mishima', 'Yukio Mishima'),
                                            ('Kazuo Ishiguro', 'Kazuo Ishiguro'),
                                            ('Junichirō Tanizaki', 'Junichirō Tanizaki')])


def generateDataFromAPI(self):
    url = "https://api.nytimes.com/svc/books/v3/reviews.json?author="
    my_key_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/api_keys.json")
    my_key = my_key_dict["my_api_key"]

    if NewsForm.author == "Haruki Murakami":
        user_author = "Haruki+Murakami"
    elif NewsForm.author == "Yukio Mishima":
        user_author = "Yukio+Mishima"
    elif NewsForm.author == "Kazuo Ishiguro":
        user_author = "Kazuo+Ishiguro"
    else:
        user_author = "Junichirō+Tanizaki"

    # Final URL
    final_url = url + user_author + "&api-key=" + my_key
    """Maybe you need to provide extra information in the API url"""
    response = requests.get(final_url).json()

    # Save info to response.json
    main_functions.save_to_file(response, "Project2_Flask/JSON_Files/response.json")
    """From the response dictionary, you need to filter the data requested by the user"""
    my_books = main_functions.read_from_file("Project2_Flask/JSON_Files/response.json")

    book_t = response.json()['results']

    book_title = []

    for b in book_t:
        title = b['book_title']
        book_title.append(title)

    return book_title
