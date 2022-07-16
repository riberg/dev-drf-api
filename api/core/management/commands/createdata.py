# Generates data for Post

from django.core.management.base import BaseCommand
from faker import Faker
from core.models import Post
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Command information'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(15):
            d = fake.unique
            Post.objects.create(
                h1=d.sentence(nb_words=5),
                title=d.sentence(nb_words=5),
                description=d.paragraph(nb_sentences=5),
                content=d.paragraph(nb_sentences=50),
                author=User.objects.get(id=1),
            )
