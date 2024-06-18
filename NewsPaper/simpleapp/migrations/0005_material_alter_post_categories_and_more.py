# Generated by Django 5.0.3 on 2024-06-17 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0004_categoryproduct_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(choices=[('article', 'Статья'), ('news', 'Новость')], to='simpleapp.category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='simpleapp.category'),
        ),
        migrations.CreateModel(
            name='ProductsMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.products')),
            ],
        ),
    ]
