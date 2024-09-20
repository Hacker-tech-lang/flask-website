from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used to secure the session

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login as Guest Route
@app.route('/login')
def login():
    session['user'] = 'Guest'  # Set the user to 'Guest'
    return redirect(url_for('profile'))

# Profile Page Route
@app.route('/profile')
def profile():
    if 'user' in session:
        user = session['user']
        return render_template('profile.html', user=user)
    else:
        return redirect(url_for('home'))

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    
  
