from django.core.management.base import BaseCommand

from catalog.models import Author

class Command(BaseCommand):
    help = 'Lists authors in the library Ax'

    def handle(self, *args, **options):
        for author in Author.objects.all():
            output = [f'{author.last_name}']

            if author.first_name:
                output.append(f', {author.first_name}')
            
            output.append(f' {author.birth_year}')

            if author.picture:
                output.append(f' {author.picture.name}')
            else:
                output.append(f' no picture')

            self.stdout.write(''.join(output))