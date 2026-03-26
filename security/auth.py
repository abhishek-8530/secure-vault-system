import bcrypt

# Store hashed password (run once and save it)
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Verify password
def check_password(entered_password, stored_hash):
    return bcrypt.checkpw(entered_password.encode(), stored_hash)