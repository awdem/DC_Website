# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Post.category'
        db.add_column(
            "hermes_post",
            "category",
            self.gf("django.db.models.fields.related.ForeignKey")(
                default=1, to=orm["hermes.Category"]
            ),
            keep_default=False,
        )

    def backwards(self, orm):
        # Deleting field 'Post.category'
        db.delete_column("hermes_post", "category_id")

    models = {
        "auth.group": {
            "Meta": {"object_name": "Group"},
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"unique": "True", "max_length": "80"},
            ),
            "permissions": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {
                    "to": "orm['auth.Permission']",
                    "symmetrical": "False",
                    "blank": "True",
                },
            ),
        },
        "auth.permission": {
            "Meta": {
                "ordering": "(u'content_type__app_label', u'content_type__model', u'codename')",
                "unique_together": "((u'content_type', u'codename'),)",
                "object_name": "Permission",
            },
            "codename": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "content_type": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {"to": "orm['contenttypes.ContentType']"},
            ),
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "50"},
            ),
        },
        "auth.user": {
            "Meta": {"object_name": "User"},
            "date_joined": (
                "django.db.models.fields.DateTimeField",
                [],
                {"default": "datetime.datetime.now"},
            ),
            "email": (
                "django.db.models.fields.EmailField",
                [],
                {"max_length": "75", "blank": "True"},
            ),
            "first_name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "30", "blank": "True"},
            ),
            "groups": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {
                    "to": "orm['auth.Group']",
                    "symmetrical": "False",
                    "blank": "True",
                },
            ),
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "is_active": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "True"},
            ),
            "is_staff": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "False"},
            ),
            "is_superuser": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "False"},
            ),
            "last_login": (
                "django.db.models.fields.DateTimeField",
                [],
                {"default": "datetime.datetime.now"},
            ),
            "last_name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "30", "blank": "True"},
            ),
            "password": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "128"},
            ),
            "user_permissions": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {
                    "to": "orm['auth.Permission']",
                    "symmetrical": "False",
                    "blank": "True",
                },
            ),
            "username": (
                "django.db.models.fields.CharField",
                [],
                {"unique": "True", "max_length": "30"},
            ),
        },
        "contenttypes.contenttype": {
            "Meta": {
                "ordering": "('name',)",
                "unique_together": "(('app_label', 'model'),)",
                "object_name": "ContentType",
                "db_table": "'django_content_type'",
            },
            "app_label": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "model": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
        },
        "hermes.category": {
            "Meta": {"object_name": "Category"},
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "parent": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {
                    "to": "orm['hermes.Category']",
                    "null": "True",
                    "blank": "True",
                },
            ),
            "title": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
        },
        "hermes.post": {
            "Meta": {"ordering": "('-created_on',)", "object_name": "Post"},
            "author": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {"to": "orm['auth.User']"},
            ),
            "body": ("django.db.models.fields.TextField", [], {}),
            "category": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {"to": "orm['hermes.Category']"},
            ),
            "created_on": (
                "django.db.models.fields.DateTimeField",
                [],
                {"auto_now_add": "True", "blank": "True"},
            ),
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "modified_on": (
                "django.db.models.fields.DateTimeField",
                [],
                {"auto_now": "True", "blank": "True"},
            ),
            "slug": (
                "django.db.models.fields.SlugField",
                [],
                {"max_length": "100"},
            ),
            "subject": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "summary": (
                "django.db.models.fields.TextField",
                [],
                {"null": "True", "blank": "True"},
            ),
        },
    }

    complete_apps = ["hermes"]
