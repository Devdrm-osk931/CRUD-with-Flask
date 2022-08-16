from flask import Blueprint, render_template, request, url_for, g, flash
from pybo.models import Message
from ..forms import MessageForm, CommentForm
from datetime import datetime
from werkzeug.utils import redirect
from .. import db
from pybo.views.auth_views import login_required

bp = Blueprint('message', __name__, url_prefix='/message')


@bp.route('/list/')
def list_msg():
    page = request.args.get('page', type=int, default=1)
    message_list = Message.query.order_by(Message.create_date.desc())
    message_list = message_list.paginate(page, per_page=10)
    return render_template('message/message_list.html', message_list=message_list)


@bp.route('/detail/<int:message_id>/')
def detail(message_id):
    form = CommentForm()
    message = Message.query.get_or_404(message_id)
    return render_template('message/message_detail.html', message=message, form=form)


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = MessageForm()
    if request.method == 'POST' and form.validate_on_submit():
        message = Message(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('message/message_form.html', form=form)


@bp.route('/modify/<int:message_id>', methods=('GET', 'POST'))
@login_required
def modify(message_id):
    message = Message.query.get_or_404(message_id)
    if g.user != message.user:
        flash("수정권한이 없습니다")
        return redirect(url_for('message.detail', message_id=message_id))
    if request.method == 'POST':
        form = MessageForm()
        if form.validate_on_submit():
            form.populate_obj(message)
            message.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('message.detail', message_id=message_id))
    else:
        form = MessageForm(obj=message)
    return render_template('message/message_form.html', form=form)


@bp.route('/delete/<int:message_id>')
@login_required
def delete(message_id):
    message = Message.query.get_or_404(message_id)
    if g.user != message.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('message.detail', message_id=message_id))
    db.session.delete(message)
    db.session.commit()
    return redirect(url_for('message.list_msg'))