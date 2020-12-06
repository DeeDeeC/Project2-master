from Project2_Flask import app, forms
from flask import request, render_template


@app.route('/', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def search():
    my_form = forms.NewsForm(request.form)

    if request.method == "POST":
        # Get the values provided by the user
        author = request.form["author"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        book_title = request.form["book_title"]

        result = forms.generateDataFromAPI(book_title)
        # this variable is assigned to the option

        """TO BE CONTINUED"""

        # Call the API
        # Generate the requested data
        return render_template('results.html',  response=result, form=my_form, author=author,
                               first_name=first_name, last_name=last_name, book_title=book_title)
    return render_template('search.html', form=my_form)

