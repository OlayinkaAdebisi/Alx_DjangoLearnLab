# update the database changing the title 
book = Book.objects.get(title = "1984")
book.title = "Nineteen Eighty-Four"
book.save()