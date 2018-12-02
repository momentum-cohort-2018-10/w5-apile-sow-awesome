from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
from linkworld.models import Post, Comment, Vote
from mimesis import Person, Text, Internet, Datetime
from random import choice
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "load posts and users dynamically"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        Post.objects.all().delete()
        Comment.objects.all().delete()
        Vote.objects.all().delete()
        users = []
        person = Person()
        for _ in range(10):
            User.objects.create(password=person.password(),     username=person.username(
            ), first_name=person.name(), last_name=person.last_name(), email=person.email())
        # date = Datetime()
        text = Text()
        internet = Internet()
        users = User.objects.all()
        for _ in range(30):
            title = text.title()
            if not Post.objects.filter(title=title).exists():
                Post.objects.create(author=choice(
                    users), text=text.text(), title=title, url=internet.home_page(), )

        posts = Post.objects.all()
        for _ in range(100):
            Comment.objects.create(commenter=choice(
                users), post=choice(posts), content=text.sentence())
            Vote.objects.create(user=choice(users), post=choice(posts))
