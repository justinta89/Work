from flask import (request, Blueprint, flash, Markup, redirect,
                   render_template, url_for)
from wtforms.fields import SelectField

from .forms import EngagementForm, QuoteForm, ApplicationForm
from .models import db, query_to_list, Engagement, Quote

default = Blueprint('default', __name__)


@default.route('/')
@default.route('/quote')
def index():
    quote_query = db.session.query(Quote)
    quotes = query_to_list(quote_query, False)

    form = QuoteForm()
    return render_template('quote.html', form=form, quotes=quotes)


@default.route('/quote/<int:id>')
@default.route('/quote/<int:id>/<template>')
def quote(id, template='engagement'):
    form = EngagementForm()
    quote = 'quote'

    if template == 'application':

        return render_template('application.html')
    else:

        return render_template('engagement.html', form=form, id=id,
                               quote=quote)

    return redirect(url_for('.index'))


@default.route('/quote/create', methods=['POST'])
def create_quote():
    form = QuoteForm(request.form)
    print(dir(form))
    if form.validate_on_submit():
        quote = Quote()
        form.populate_obj(quote)
        db.session.add(quote)
        db.session.commit()
        return redirect(url_for('.quote', id=quote.id))
    return render_template('validation_error.html', form=form)


@default.route('/quote/<quote_id>/engagement/', methods=['GET'])
@default.route('/quote/<quote_id>/engagement/<int:id>', methods=['GET'])
def engagement(quote_id, id):
    engagements_query = db.session.query(Engagement).filter_by(
        id=id, quote_id=quote_id)

    if not engagements_query:
        return redirect(url_for('.quote', id=quote_id))
    form = EngagementForm()

    engagements = query_to_list(engagements_query, False)
    return render_template('engagement.html', engagements=engagements,
                           dir=dir, form=form)


@default.route('/engagement/create', methods=['POST'])
def create_engagement():
    form = EngagementForm()
    if form.validate_on_submit():
        engagement = Engagement()
        form.populate_obj(engagement)
        db.session.add(engagement)
        db.session.commit()
        return redirect(url_for('.quote'))

    return render_template('engagement.html', form=form)
