# update the database changing the title 
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
