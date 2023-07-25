```python
from flask import render_template, url_for, flash, redirect, request
from mindscribe import app, db, login_manager
from mindscribe.forms import RegistrationForm, LoginForm, NoteForm, SummaryForm, ChatForm, MusicForm
from mindscribe.models import User, Note, Summary, Chat, Music
from flask_login import login_user, current_user, logout_user, login_required
from mindscribe.utils.token_manager import update_tokens, check_tokens

@app.route("/")
@app.route("/landing")
def landing():
    return render_template('landing.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('content'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, tokens=5)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'register-success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('content'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'login-success')
            return redirect(url_for('content'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'login-error')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('landing'))

@app.route("/content")
@login_required
def content():
    return render_template('content.html', title='Content')

@app.route("/note_maker", methods=['GET', 'POST'])
@login_required
def note_maker():
    form = NoteForm()
    if form.validate_on_submit():
        if check_tokens(current_user):
            note = Note(title=form.title.data, content=form.content.data, user_id=current_user.id)
            db.session.add(note)
            db.session.commit()
            update_tokens(current_user)
            flash('Your note has been created!', 'note-success')
        else:
            flash('You have no tokens left!', 'note-error')
    return render_template('note_maker.html', title='Note Maker', form=form)

@app.route("/summarizer", methods=['GET', 'POST'])
@login_required
def summarizer():
    form = SummaryForm()
    if form.validate_on_submit():
        if check_tokens(current_user):
            summary = Summary(url=form.url.data, summary=form.summary.data, user_id=current_user.id)
            db.session.add(summary)
            db.session.commit()
            update_tokens(current_user)
            flash('Your summary has been created!', 'summary-success')
        else:
            flash('You have no tokens left!', 'summary-error')
    return render_template('summarizer.html', title='Summarizer', form=form)

@app.route("/chatbot", methods=['GET', 'POST'])
@login_required
def chatbot():
    form = ChatForm()
    if form.validate_on_submit():
        if check_tokens(current_user):
            chat = Chat(question=form.question.data, answer=form.answer.data, user_id=current_user.id)
            db.session.add(chat)
            db.session.commit()
            update_tokens(current_user)
            flash('Your chat has been started!', 'chat-success')
        else:
            flash('You have no tokens left!', 'chat-error')
    return render_template('chatbot.html', title='Chatbot', form=form)

@app.route("/music_generator", methods=['GET', 'POST'])
@login_required
def music_generator():
    form = MusicForm()
    if form.validate_on_submit():
        if check_tokens(current_user):
            music = Music(settings=form.settings.data, user_id=current_user.id)
            db.session.add(music)
            db.session.commit()
            update_tokens(current_user)
            flash('Your music has been generated!', 'music-success')
        else:
            flash('You have no tokens left!', 'music-error')
    return render_template('music_generator.html', title='Music Generator', form=form)
```