#!/usr/bin/python3
"""User class"""


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def is_valid_password(self, password):
        return password == self.password
