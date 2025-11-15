#create a table using sqlite
new_book = Book.objects.create(title='1984', author='George Orwell', published_year='1949')
new_book.save()