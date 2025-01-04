from django.apps import AppConfig

class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

    def ready(self):
        # Import and run the migration script when the app is ready
        from .migrations import insert_initial_books
        insert_initial_books()
