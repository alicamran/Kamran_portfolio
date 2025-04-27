from flask import Flask, render_template, redirect, url_for, session
from forms import BookingForm
from models import categories, subcategories

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookingForm()
    # Populate category dropdown
    form.category.choices = categories
    # Populate subcategory based on selected category
    if form.category.data:
        form.subcategory.choices = subcategories.get(form.category.data, [])
    else:
        form.subcategory.choices = []

    if form.validate_on_submit():
        # Store booking details in session
        booking = {
            'name': form.name.data,
            'email': form.email.data,
            'phone': form.phone.data,
            'category': form.category.data,
            'subcategory': form.subcategory.data,
            'price': next(price for name, price in subcategories[form.category.data] if name == form.subcategory.data),
            'appointment': form.appointment.data.strftime('%Y-%m-%d %H:%M')
        }
        session['booking'] = booking
        return redirect(url_for('cart_view'))

    return render_template('index.html', form=form, subcategories=subcategories)

@app.route('/cart')
def cart_view():
    booking = session.get('booking')
    return render_template('cart.html', booking=booking)

if __name__ == '__main__':
    app.run(debug=True)