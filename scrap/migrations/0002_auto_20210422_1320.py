# Generated by Django 3.2 on 2021-04-22 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapModelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(blank=True, max_length=255, null=True)),
                ('photo_room', models.CharField(blank=True, max_length=1, null=True)),
                ('bathroom', models.TextField(blank=True, null=True)),
                ('room_view_title', models.TextField(blank=True, null=True)),
                ('equipment_title', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='scrapmodel',
            old_name='hotelName',
            new_name='address_hotel',
        ),
        migrations.RenameField(
            model_name='scrapmodel',
            old_name='reviews',
            new_name='name_hotel',
        ),
        migrations.RenameField(
            model_name='scrapmodel',
            old_name='address',
            new_name='photo_hotel',
        ),
        migrations.RenameField(
            model_name='scrapmodel',
            old_name='roomName',
            new_name='review_quantities',
        ),
        migrations.RemoveField(
            model_name='scrapmodel',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='scrapmodel',
            name='qualification',
        ),
        migrations.AddField(
            model_name='scrapmodel',
            name='review_score',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='ScrapModelPhotos',
        ),
        migrations.AddField(
            model_name='scrapmodelroom',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrap.scrapmodel'),
        ),
    ]
