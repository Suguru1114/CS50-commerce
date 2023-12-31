# Generated by Django 4.2 on 2023-11-04 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_current_highest_bid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='categoryName',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='Uncategorized', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='auctions.category'),
        ),
    ]
