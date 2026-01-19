#!/usr/bin/env python3
# airflow-init.py
from airflow.auth.backends.basic import hashed_password
from airflow import settings
from airflow.models import User

session = settings.Session()
existing = session.query(User).filter(User.username == "admin").first()
if existing:
    print("Admin user already exists.")
else:
    u = User(
        username="admin",
        email="admin@example.com",
        password=hashed_password("admin"),
        role="Admin",
    )
    session.add(u)
    session.commit()
    print("Created admin user.")
