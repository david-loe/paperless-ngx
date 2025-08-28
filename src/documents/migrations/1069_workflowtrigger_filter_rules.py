import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1068_alter_document_created"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkflowTriggerFilterRule",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rule_type",
                    models.PositiveIntegerField(verbose_name="rule type"),
                ),
                (
                    "value",
                    models.CharField(
                        verbose_name="value",
                        max_length=255,
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "workflow_trigger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="filter_rules",
                        to="documents.workflowtrigger",
                        verbose_name="workflow trigger",
                    ),
                ),
            ],
            options={
                "verbose_name": "workflow trigger filter rule",
                "verbose_name_plural": "workflow trigger filter rules",
            },
        ),
    ]
