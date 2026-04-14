from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'studyai-secret-2025'

# ── Fake user store (replace with DB later) ──────────────────
USERS = {}  # { username: password }

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ── Routes ───────────────────────────────────────────────────

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        if username in USERS and USERS[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    success = None
    if request.method == 'POST':
        first    = request.form.get('first', '').strip()
        last     = request.form.get('last', '').strip()
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        confirm  = request.form.get('confirm', '')
        if not all([first, last, username, password, confirm]):
            error = 'Please fill in all fields.'
        elif password != confirm:
            error = 'Passwords do not match.'
        elif len(password) < 8:
            error = 'Password must be at least 8 characters.'
        elif username in USERS:
            error = 'Username already taken.'
        else:
            USERS[username] = password
            session['username'] = username
            session['fullname'] = first + ' ' + last
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error, tab='register')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    name = session.get('fullname', session.get('username', 'Student'))
    return render_template('dashboard.html', username=name, active='dashboard')

@app.route('/calendar')
@login_required
def calendar():
    name = session.get('fullname', session.get('username', 'Student'))
    return render_template('calendar.html', username=name, active='calendar')

@app.route('/progress')
@login_required
def progress():
    name = session.get('fullname', session.get('username', 'Student'))
    return render_template('progress.html', username=name, active='progress')

@app.route('/download')
@login_required
def download():
    name = session.get('fullname', session.get('username', 'Student'))
    return render_template('download.html', username=name, active='download')

if __name__ == '__main__':
    app.run(debug=True)
