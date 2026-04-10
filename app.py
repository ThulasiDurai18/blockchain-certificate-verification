# from flask import Flask, render_template, request, redirect, url_for, session, flash
# import sqlite3

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'


# import os
# from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure upload directory exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS













# # Create DB and table for students
# # def init_db():
# #     conn = sqlite3.connect('db.sqlite3')
# #     c = conn.cursor()
# #     c.execute('''
# #         CREATE TABLE IF NOT EXISTS students (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             username TEXT UNIQUE,
# #             password TEXT
# #         )
# #     ''')
# #     conn.commit()
# #     conn.close()

# # def init_db():
# #     conn = sqlite3.connect('db.sqlite3')
# #     c = conn.cursor()
# #     c.execute('''
# #         CREATE TABLE IF NOT EXISTS students (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             username TEXT UNIQUE,
# #             password TEXT
# #         )
# #     ''')
# #     c.execute('''
# #         CREATE TABLE IF NOT EXISTS certificates (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             student_id INTEGER,
# #             name TEXT,
# #             email TEXT,
# #             phone TEXT,
# #             department TEXT,
# #             degree TEXT,
# #             status TEXT DEFAULT 'Pending',
# #             FOREIGN KEY (student_id) REFERENCES students(id)
# #         )
# #     ''')
# #     conn.commit()
# #     conn.close()


# import sqlite3


# def init_db():
#     """Initialize the SQLite database and create tables if they don't exist."""
#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()

#     # ✅ Enable foreign key constraints (important for SQLite)
#     c.execute("PRAGMA foreign_keys = ON;")

#     # ✅ Create Students table
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         );
#     ''')

#     # ✅ Create Certificates table (with file_path for uploads)
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS certificates (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             student_id INTEGER NOT NULL,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL,
#             phone TEXT NOT NULL,
#             department TEXT NOT NULL,
#             degree TEXT NOT NULL,
#             file_path TEXT,                     -- stores uploaded PDF/image path
#             status TEXT DEFAULT 'Pending',
#             admin_status TEXT DEFAULT 'Pending',
#             FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
#         );
#     ''')

#     conn.commit()
#     conn.close()
#     print("✅ Database initialized successfully with all required tables.")




# def add_admin_status_column():
#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()
#     # Check if column exists (optional, to avoid duplicates)
#     c.execute("PRAGMA table_info(certificates)")
#     columns = [col[1] for col in c.fetchall()]
#     if 'admin_status' not in columns:
#         c.execute("ALTER TABLE certificates ADD COLUMN admin_status TEXT DEFAULT 'Pending'")
#         conn.commit()
#     conn.close()


# init_db()
# add_admin_status_column()
# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     role = request.args.get('role')
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         if role == 'admin':
#             if username == 'admin' and password == 'admin123':
#                 session['user'] = 'admin'
#                 return redirect('/admin-dashboard')
#             else:
#                 flash('Invalid admin credentials')

#         elif role == 'verifier':
#             if username == 'verifier' and password == 'verifier123':
#                 session['user'] = 'verifier'
#                 return redirect('/verifier-dashboard')
#             else:
#                 flash('Invalid verifier credentials')

#         elif role == 'student':
#             conn = sqlite3.connect('db.sqlite3')
#             c = conn.cursor()
#             c.execute("SELECT * FROM students WHERE username=? AND password=?", (username, password))
#             user = c.fetchone()
#             conn.close()
#             if user:
#                 session['user'] = username
#                 return redirect('/dashboard')
#             else:
#                 flash('Invalid student credentials')

#     return render_template('login.html', role=role)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = sqlite3.connect('db.sqlite3')
#         c = conn.cursor()
#         try:
#             c.execute("INSERT INTO students (username, password) VALUES (?, ?)", (username, password))
#             conn.commit()
#             flash("Registration successful! Please log in.")
#             return redirect(url_for('login', role='student'))
#         except sqlite3.IntegrityError:
#             flash("Username already exists.")
#         finally:
#             conn.close()
#     return render_template('register.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html', user=session.get('user'))

# # @app.route('/verifier-dashboard')
# # def verifier_dashboard():
# #     return render_template('verifier_dashboard.html', user=session.get('user'))


# # @app.route('/submit-academic', methods=['GET', 'POST'])
# # def submit_academic():
# #     if 'user' not in session:
# #         return redirect('/')
    
# #     username = session['user']
# #     conn = sqlite3.connect('db.sqlite3')
# #     c = conn.cursor()
# #     c.execute("SELECT id FROM students WHERE username=?", (username,))
# #     student = c.fetchone()
# #     if not student:
# #         flash("Student not found.")
# #         return redirect('/dashboard')
# #     student_id = student[0]

# #     if request.method == 'POST':
# #         name = request.form['name']
# #         email = request.form['email']
# #         phone = request.form['phone']
# #         department = request.form['department']
# #         degree = request.form['degree']

# #         c.execute('''
# #             INSERT INTO certificates (student_id, name, email, phone, department, degree)
# #             VALUES (?, ?, ?, ?, ?, ?)
# #         ''', (student_id, name, email, phone, department, degree))
# #         conn.commit()
# #         flash('Academic details submitted!')
# #         return redirect('/dashboard')

# #     conn.close()
# #     return render_template('submit_academic.html')


# @app.route('/submit-academic', methods=['GET', 'POST'])
# def submit_academic():
#     if 'user' not in session:
#         return redirect('/')

#     username = session['user']
#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()
#     c.execute("SELECT id FROM students WHERE username=?", (username,))
#     student = c.fetchone()
#     if not student:
#         flash("Student not found.")
#         conn.close()
#         return redirect('/dashboard')

#     student_id = student[0]

#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         department = request.form['department']
#         degree = request.form['degree']

#         file = request.files.get('certificate_file')
#         if not file:
#             flash("No file uploaded.")
#             conn.close()
#             return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)
#         else:
#             flash("Invalid file type. Please upload PDF or image.")
#             conn.close()
#             return redirect(request.url)

#         c.execute('''
#             INSERT INTO certificates (student_id, name, email, phone, department, degree, file_path)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (student_id, name, email, phone, department, degree, filepath))
#         conn.commit()
#         conn.close()

#         flash('Academic details and certificate uploaded successfully!')
#         return redirect('/dashboard')

#     conn.close()
#     return render_template('submit_academic.html')


# @app.route('/verifier-dashboard')
# def verifier_dashboard():
#     if session.get('user') != 'verifier':
#         return redirect('/')

#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()
#     c.execute('''
#         SELECT certificates.id, students.username, name, email, phone, department, degree, status 
#         FROM certificates
#         JOIN students ON certificates.student_id = students.id
#     ''')
#     records = c.fetchall()
#     conn.close()
#     return render_template('verifier_dashboard.html', records=records)


# @app.route('/update-status/<int:cert_id>/<action>')
# def update_status(cert_id, action):
#     if session.get('user') != 'verifier':
#         return redirect('/')

#     status = 'Verified' if action == 'verify' else 'Rejected'
#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()
#     c.execute("UPDATE certificates SET status=? WHERE id=?", (status, cert_id))
#     conn.commit()
#     conn.close()
#     return redirect('/verifier-dashboard')

# @app.route('/view-status')
# def view_status():
#     if 'user' not in session:
#         return redirect('/login?role=student')

#     username = session['user']
#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()

#     c.execute("SELECT id FROM students WHERE username=?", (username,))
#     student = c.fetchone()
#     if not student:
#         flash("Student not found.")
#         return redirect('/dashboard')
#     student_id = student[0]

#     c.execute('''
#         SELECT name, email, phone, department, degree, status, admin_status
#         FROM certificates WHERE student_id=?
#     ''', (student_id,))
#     records = c.fetchall()
#     conn.close()

#     return render_template('view_status.html', records=records)


# # @app.route('/view-status')
# # def view_status():
# #     if 'user' not in session:
# #         return redirect('/login?role=student')

# #     username = session['user']
# #     conn = sqlite3.connect('db.sqlite3')
# #     c = conn.cursor()

# #     # Get student id
# #     c.execute("SELECT id FROM students WHERE username=?", (username,))
# #     student = c.fetchone()
# #     if not student:
# #         flash("Student not found.")
# #         return redirect('/dashboard')
# #     student_id = student[0]

# #     # Get certificates for this student
# #     c.execute('''
# #         SELECT name, email, phone, department, degree, status
# #         FROM certificates WHERE student_id=?
# #     ''', (student_id,))
# #     records = c.fetchall()
# #     conn.close()

# #     return render_template('view_status.html', records=records)


# # @app.route('/admin-dashboard')
# # def admin_dashboard():
# #     if session.get('user') != 'admin':
# #         return redirect('/')

# #     conn = sqlite3.connect('db.sqlite3')
# #     c = conn.cursor()
# #     c.execute('''
# #         SELECT certificates.id, students.username, name, email, phone, department, degree, status, admin_status
# #         FROM certificates
# #         JOIN students ON certificates.student_id = students.id
# #         WHERE status = 'Verified' AND admin_status = 'Pending'
# #     ''')
# #     records = c.fetchall()
# #     conn.close()
# #     return render_template('admin_dashboard.html', records=records)

# @app.route('/admin-dashboard')
# def admin_dashboard():
#     if session.get('user') != 'admin':
#         return redirect('/')
    
#     # Fetch certificate records needing admin approval
#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()
#     c.execute('''
#         SELECT certificates.id, students.username, certificates.name, certificates.email, certificates.phone,
#                certificates.department, certificates.degree, certificates.status, certificates.admin_status
#         FROM certificates
#         JOIN students ON certificates.student_id = students.id
#         WHERE certificates.status = 'Verified' AND certificates.admin_status = 'Pending'
#     ''')
#     records = c.fetchall()
#     conn.close()
#     return render_template('admin_dashboard.html', records=records)


# @app.route('/admin-update-status/<int:cert_id>/<action>')
# def admin_update_status(cert_id, action):
#     if session.get('user') != 'admin':
#         return redirect('/')

#     status = 'Approved' if action == 'approve' else 'Rejected'
#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()
#     c.execute("UPDATE certificates SET admin_status=? WHERE id=?", (status, cert_id))
#     conn.commit()
#     conn.close()
#     return redirect('/admin-dashboard')


# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from werkzeug.utils import secure_filename

# ------------------------
# Flask app config
# ------------------------
app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ------------------------
# RSA encryption imports
# ------------------------
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend



# ------------------------
# Utility functions
# ------------------------
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def encrypt_file(file_path, client_name):
    # Load RSA public key
    public_key_path = "public.pem"
    if not os.path.exists(public_key_path):
        raise FileNotFoundError("Public key not found. Please generate 'public.pem'.")

    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Read file content
    with open(file_path, "rb") as f:
        data = f.read()

    # Generate random AES key
    aes_key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)       # 128-bit IV

    # Encrypt data with AES
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    # Encrypt AES key with RSA
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save encrypted file: [RSA-encrypted key + IV + AES-encrypted data]
    ext = os.path.splitext(file_path)[1]
    encrypted_filename = f"{client_name}{ext}.enc"
    encrypted_path = os.path.join(os.path.dirname(file_path), encrypted_filename)

    with open(encrypted_path, "wb") as f:
        f.write(len(encrypted_key).to_bytes(4, 'big'))  # store key length
        f.write(encrypted_key)                           # RSA-encrypted AES key
        f.write(iv)                                      # IV
        f.write(encrypted_data)                          # AES-encrypted file

    return encrypted_path

# def encrypt_file(filepath):
#     """Encrypt a file using RSA public key"""
#     with open("public.pem", "rb") as f:
#         public_key = RSA.import_key(f.read())
#     cipher = PKCS1_OAEP.new(public_key)

#     with open(filepath, "rb") as f:
#         data = f.read()

#     # RSA can only encrypt small chunks
#     chunk_size = 190
#     encrypted_data = b''
#     for i in range(0, len(data), chunk_size):
#         chunk = data[i:i+chunk_size]
#         encrypted_data += cipher.encrypt(chunk)

#     encrypted_path = filepath + ".enc"
#     with open(encrypted_path, "wb") as f:
#         f.write(encrypted_data)

#     os.remove(filepath)
#     return encrypted_path

# ------------------------
# Database initialization
# ------------------------
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")

    # Students table
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    ''')

    # Certificates table
    c.execute('''
        CREATE TABLE IF NOT EXISTS certificates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL,
            degree TEXT NOT NULL,
            file_path TEXT,
            status TEXT DEFAULT 'Pending',
            admin_status TEXT DEFAULT 'Pending',
            FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
        );
    ''')
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully.")

init_db()

# ------------------------
# Routes
# ------------------------
@app.route('/')
def home():
    return render_template('home.html')

# ------------------------
# Login & Register
# ------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    role = request.args.get('role')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if role == 'admin':
            if username == 'admin' and password == 'admin123':
                session['user'] = 'admin'
                return redirect('/admin-dashboard')
            else:
                flash('Invalid admin credentials')

        elif role == 'verifier':
            if username == 'verifier' and password == 'verifier123':
                session['user'] = 'verifier'
                return redirect('/verifier-dashboard')
            else:
                flash('Invalid verifier credentials')

        elif role == 'student':
            conn = sqlite3.connect('db.sqlite3')
            c = conn.cursor()
            c.execute("SELECT * FROM students WHERE username=? AND password=?", (username, password))
            user = c.fetchone()
            conn.close()
            if user:
                session['user'] = username
                return redirect('/dashboard')
            else:
                flash('Invalid student credentials')

    return render_template('login.html', role=role)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO students (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("Registration successful! Please log in.")
            return redirect(url_for('login', role='student'))
        except sqlite3.IntegrityError:
            flash("Username already exists.")
        finally:
            conn.close()
    return render_template('register.html')

# ------------------------
# Student Dashboard
# ------------------------
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', user=session.get('user'))

# ------------------------
# Submit academic details + upload certificate
# ------------------------
# @app.route('/submit-academic', methods=['GET', 'POST'])
# def submit_academic():
#     if 'user' not in session:
#         return redirect('/')

#     username = session['user']
#     conn = sqlite3.connect('db.sqlite3')
#     c = conn.cursor()
#     c.execute("SELECT id FROM students WHERE username=?", (username,))
#     student = c.fetchone()
#     if not student:
#         flash("Student not found.")
#         conn.close()
#         return redirect('/dashboard')

#     student_id = student[0]

#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         department = request.form['department']
#         degree = request.form['degree']

#         file = request.files.get('certificate_file')
#         if not file:
#             flash("No file uploaded.")
#             conn.close()
#             return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)
#             # Encrypt the uploaded file
#             encrypted_path = encrypt_file(filepath)
#         else:
#             flash("Invalid file type. Please upload PDF or image.")
#             conn.close()
#             return redirect(request.url)

#         c.execute('''
#             INSERT INTO certificates (student_id, name, email, phone, department, degree, file_path)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (student_id, name, email, phone, department, degree, encrypted_path))
#         conn.commit()
#         conn.close()
#         flash('Academic details and certificate uploaded successfully!')
#         return redirect('/dashboard')

#     conn.close()
#     return render_template('submit_academic.html')
@app.route('/submit-academic', methods=['GET', 'POST'])
def submit_academic():
    if 'user' not in session:
        return redirect('/')

    username = session['user']
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT id FROM students WHERE username=?", (username,))
    student = c.fetchone()
    if not student:
        flash("Student not found.")
        conn.close()
        return redirect('/dashboard')

    student_id = student[0]

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form['department']
        degree = request.form['degree']

        file = request.files.get('certificate_file')
        if not file:
            flash("No file uploaded.")
            conn.close()
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # ✅ Encrypt the file using client name
            encrypted_path = encrypt_file(filepath, name)
        else:
            flash("Invalid file type. Please upload PDF or image.")
            conn.close()
            return redirect(request.url)

        c.execute('''
            INSERT INTO certificates (student_id, name, email, phone, department, degree, file_path)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (student_id, name, email, phone, department, degree, encrypted_path))
        conn.commit()
        conn.close()

        flash('Academic details submitted and file encrypted successfully!')
        return redirect('/dashboard')

    conn.close()
    return render_template('submit_academic.html')

# ------------------------
# Verifier Dashboard
# ------------------------
@app.route('/verifier-dashboard')
def verifier_dashboard():
    if session.get('user') != 'verifier':
        return redirect('/')

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('''
        SELECT certificates.id, students.username, name, email, phone, department, degree, status 
        FROM certificates
        JOIN students ON certificates.student_id = students.id
    ''')
    records = c.fetchall()
    conn.close()
    return render_template('verifier_dashboard.html', records=records)

@app.route('/update-status/<int:cert_id>/<action>')
def update_status(cert_id, action):
    if session.get('user') != 'verifier':
        return redirect('/')

    status = 'Verified' if action == 'verify' else 'Rejected'
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("UPDATE certificates SET status=? WHERE id=?", (status, cert_id))
    conn.commit()
    conn.close()
    return redirect('/verifier-dashboard')

# ------------------------
# View status (Student)
# ------------------------
@app.route('/view-status')
def view_status():
    if 'user' not in session:
        return redirect('/login?role=student')

    username = session['user']
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    c.execute("SELECT id FROM students WHERE username=?", (username,))
    student = c.fetchone()
    if not student:
        flash("Student not found.")
        return redirect('/dashboard')
    student_id = student[0]

    c.execute('''
        SELECT name, email, phone, department, degree, status, admin_status
        FROM certificates WHERE student_id=?
    ''', (student_id,))
    records = c.fetchall()
    conn.close()
    return render_template('view_status.html', records=records)

# ------------------------
# Admin Dashboard
# ------------------------
@app.route('/admin-dashboard')
def admin_dashboard():
    if session.get('user') != 'admin':
        return redirect('/')

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('''
        SELECT certificates.id, students.username, certificates.name, certificates.email, certificates.phone,
               certificates.department, certificates.degree, certificates.status, certificates.admin_status
        FROM certificates
        JOIN students ON certificates.student_id = students.id
        WHERE certificates.status = 'Verified' AND certificates.admin_status = 'Pending'
    ''')
    records = c.fetchall()
    conn.close()
    return render_template('admin_dashboard.html', records=records)

@app.route('/admin-update-status/<int:cert_id>/<action>')
def admin_update_status(cert_id, action):
    if session.get('user') != 'admin':
        return redirect('/')

    status = 'Approved' if action == 'approve' else 'Rejected'
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("UPDATE certificates SET admin_status=? WHERE id=?", (status, cert_id))
    conn.commit()
    conn.close()
    return redirect('/admin-dashboard')

# ------------------------
# Logout
# ------------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# ------------------------
# Run Flask App
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
