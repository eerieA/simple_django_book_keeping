from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser

from catalog.models import Book

class Command(BaseCommand):
    help = 'Show book info in the library Ax'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--all', action='store_true', help='List all books')
        
        parser.add_argument('book_ids', nargs='*', type=int, help='IDs of books to show')

    def handle(self, *args: Any, **options: Any) -> str | None:
        if options['all']:
            books = Book.objects.all()
        elif options['book_ids']:
            books = Book.objects.filter(id__in=options['book_ids'])
        else:
            raise CommandError('Must provide a book id or --all argument')
        
        for book in books:
            output = [f'{book.title}, {book.author.last_name}']

            if book.author.first_name:
                output.append(f', {book.author.first_name}')

            output.append(f' [id={book.id}]')

            self.stdout.write(''.join(output))