from flask import Blueprint, flash, Markup, redirect, render_template, url_for

from .forms import EngagementForm
from .models import db, query_to_list, Engagement

default = Blueprint('default', __name__)


@default.route('/')
def index():
    return 'helo'
    # sample_form = SampleForm()
    # names_query = db.session.query(Sample)
    # names = [row[1] for row in query_to_list(names_query, False)]
    # return render_template('index.html', names=names, sample_form=sample_form)


# @default.route('/sample', methods=['POST'])
# def sample():
#     form = SampleForm()
#     if form.validate_on_submit():
#         sample = Sample()
#         form.populate_obj(sample)
#         db.session.add(sample)
#         db.session.commit()
#         return redirect(url_for('.index'))
# 
#     return render_template('validation_error.html', form=form)
