from flask import render_template, Blueprint, redirect, request
from app.shipping_form import ShippingForm
bp = Blueprint('main', __name__, template_folder='../templates')
from app.model import db, Package

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    print(f"Request method: {request.method}")  # Add this

    if form.validate_on_submit():
        print("Form validated successfully")  # Add this
        package = Package(
            sender=form.sender.data,
            recipient=form.recipient.data,
            origin=form.origin.data,
            destination=form.destination.data,
            location=form.origin.data
        )
        db.session.add(package)
        db.session.commit()
        return redirect('/')

    if form.errors:  # Add this
        print(f"Form validation errors: {form.errors}")

    return render_template('shipping_request.html', form=form)
