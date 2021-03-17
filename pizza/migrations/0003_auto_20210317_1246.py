# Generated by Django 2.2.5 on 2021-03-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20210317_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='PizzaName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza_name',
        ),
        migrations.AddField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]