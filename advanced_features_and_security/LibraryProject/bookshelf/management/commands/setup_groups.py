# bookshelf/management/commands/setup_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Creates default user groups with permissions'

    def handle(self, *args, **options):
        # Get the content type for the Book model
        try:
            content_type = ContentType.objects.get_for_model(Book)
        except ContentType.DoesNotExist:
            self.stdout.write(self.style.ERROR('ContentType for Book model not found!'))
            return

        # Ensure all permissions exist
        permissions_map = {
            'can_view_book': 'Can view book',
            'can_create_book': 'Can create book',
            'can_edit_book': 'Can edit book',
            'can_delete_book': 'Can delete book',
        }

        permissions = {}
        for codename, name in permissions_map.items():
            perm, created = Permission.objects.get_or_create(
                codename=codename,
                name=name,
                content_type=content_type
            )
            permissions[codename] = perm
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created permission: {codename}'))

        # Define groups and their permissions
        groups = {
            'Viewers': ['can_view_book'],
            'Editors': ['can_view_book', 'can_create_book', 'can_edit_book'],
            'Admins': ['can_view_book', 'can_create_book', 'can_edit_book', 'can_delete_book'],
        }

        # Create groups and assign permissions
        for group_name, permission_codenames in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in permission_codenames:
                group.permissions.add(permissions[codename])
            self.stdout.write(self.style.SUCCESS(f'Configured group: {group_name}'))

        self.stdout.write(self.style.SUCCESS('Successfully set up all groups and permissions!'))