from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect
from datetime import datetime
from pybo import db
from pybo.models import Message, Comment
from ..forms import CommentForm
from .auth_views import login_required


bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/create/<int:message_id>', methods=('POST',))
@login_required
def create(message_id):
    form = CommentForm()
    message = Message.query.get_or_404(message_id)
    if form.validate_on_submit():
        content = request.form['content']
        comment = Comment(content=content, create_date=datetime.now(), user=g.user)
        message.comment_set.append(comment)
        db.session.commit()
        return redirect(url_for('message.detail', message_id=message_id))
    return render_template('message/message_detail.html', message=message, form=form)


@bp.route('/delete/<int:comment_id>')
@login_required
def delete(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    message_id = comment.message_id
    if g.user != comment.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('message.detail', message_id=message_id))
