def setUp(self):
Here i sign in a User, create an author for the DB, login a user asper checker requirememt

def test_get_books(self)
Sends a GET to view objects in Book
returns 200 

def test_create_books(self)
uses POST
force authenticate a user asper authentication included in views
returns 201

def test_update_books(self):
sends a PUT
force authenticate them confirms the updated title
returns 200

def test_delete_books(self):
sends a delete
returns 204