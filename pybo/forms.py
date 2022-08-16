from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class MessageForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired("제목을 입력하세요!")])
    content = TextAreaField('내용', validators=[DataRequired("내용을 입력하세요!")])


class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired("내용을 입력하세요!")])


class RegisterForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired("아이디는 필수 입력 사항입니다!"), Length(min=1, max=20)])
    password1 = PasswordField('비밀번호', validators=[DataRequired("비밀번호는 필수 입력 사항입니다!"), EqualTo('password2', '입력한 비밀번호가 일치하지 않습니다!')])
    password2 = PasswordField('비밀번호확인', validators=[(DataRequired("비밀번호 재입력은 필수 입력사항입니다!"))])
    email = EmailField('이메일', validators=[DataRequired(), Email("이메일은 필수 입력사항입니다!")])


class LoginForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired()])