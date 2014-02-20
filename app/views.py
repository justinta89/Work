from flask import Blueprint, flash, Markup, redirect, render_template, url_for

from .forms import EngagementForm, ApplicationForm
from .models import db, query_to_list, Engagement

default = Blueprint('default', __name__)


@default.route('/')
def index():
    form = EngagementForm()
    engagements_query = db.session.query(Engagement)
    engagements = query_to_list(engagements_query, False)
    return render_template('index.html', form=form, engagements=engagements)


@default.route('/engagement/create', methods=['POST'])
def create_engagement():
    form = EngagementForm()
    if form.validate_on_submit():
        engagement = Engagement()
        form.populate_obj(engagement)
        db.session.add(engagement)
        db.session.commit()
        return redirect(url_for('.index'))

    return render_template('engagement.html', form=form)


@default.route('/quote/', methods=['GET'])
def quote():
    pass


@default.route('/quote/create', methods=['POST'])
def create_quote():
    pass
