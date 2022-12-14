# Generated by Django 4.1.2 on 2022-10-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="dados",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=2)),
                ("data", models.CharField(max_length=8)),
                ("valor", models.CharField(max_length=10)),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=12)),
                ("hora", models.CharField(max_length=6)),
                ("dono_da_loja", models.CharField(max_length=14)),
                ("nome_loja", models.CharField(max_length=19)),
            ],
        ),
    ]
