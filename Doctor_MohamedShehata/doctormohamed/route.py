from flask import  render_template,url_for,flash,redirect
from doctormohamed.forum import RegistrationForm , LoginForm
from doctormohamed.models import PatientVisits, Patient
from  doctormohamed import app,db,bcrypt

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title= "Home Page")

@app.route("/about")
def about():
    return render_template('about.html',title="About Page")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
         hashed_passwd = bcrypt.generate_password_hash(form.password.data).decode('utf8')
         user = Patient(username=form.username.data,email=form.email.data,password=hashed_passwd)
         db.session.add(user)
         db.session.commit()
         flash('You Dental Account has been created! You are now able to log in','success')
         return redirect(url_for('login'))
    return render_template('register.html',title="Register patient Page", form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("you have logged in !!",'success')
            return redirect(url_for('home'))
        else:
            flash("login unsuccessful. Please check username and password",'danger')
    return render_template('login.html',title="My Chart Login", form=form)
