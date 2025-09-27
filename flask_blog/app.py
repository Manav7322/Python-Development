from flask import Flask, request, session, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

app.secret_key = "supersecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)
    likes = db.relationship("Like", backref="user", lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime(timezone=True), server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    likes = db.relationship("Like", backref="post", lazy=True)


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return redirect(url_for('posts'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return render_template("register.html", error="Username or Email already exists. Please login instead.")
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
        return redirect(url_for("posts"))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()

        if user:
            session["user_id"] = user.id
            return redirect(url_for("posts"))
        else:
            return render_template("login.html", error="Username not found. Please register first.")
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('posts'))


@app.route('/posts', methods=['GET'])
def posts():
    all_posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template("posts.html", posts=all_posts)


@app.route('/like/<int:post_id>', methods=['POST'])
def like_post(post_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    
    existing_like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
    if existing_like:
        # Unlike the post
        db.session.delete(existing_like)
        db.session.commit()
    else:
        # Like the post
        new_like = Like(user_id=user_id, post_id=post_id)
        db.session.add(new_like)
        db.session.commit()
    return redirect(url_for("posts"))


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    if request.method == 'POST':
        title = request.form["title"]
        content = request.form["content"]
        new_post = Post(title=title, content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("posts"))
    
    return render_template("add_post.html")


if __name__ == "__main__":
    app.run(debug=True)