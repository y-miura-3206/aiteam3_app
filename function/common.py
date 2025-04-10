import streamlit as st
import yaml
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def load_user_data():
    with open('.vscode/config.yaml', 'r') as f:
        return yaml.safe_load(f) or {}

def save_user_data(user_data):
    with open('.vscode/config.yaml', 'w') as f:
        yaml.dump(user_data, f)