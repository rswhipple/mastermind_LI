# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Players(models.Model):
    player_id = models.AutoField(primary_key=True, blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players'


class Games(models.Model):
    game_id = models.AutoField(primary_key=True, blank=True, null=True)
    player = models.ForeignKey('Player', models.DO_NOTHING, blank=True, null=True)
    start_time = models.TextField(blank=True, null=True)
    end_time = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Losses(models.Model):
    loss_id = models.AutoField(primary_key=True, blank=True, null=True)
    player = models.ForeignKey('Player', models.DO_NOTHING, blank=True, null=True)
    game = models.ForeignKey('Game', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'losses'


class Wins(models.Model):
    win_id = models.AutoField(primary_key=True, blank=True, null=True)
    player = models.ForeignKey('Player', models.DO_NOTHING, blank=True, null=True)
    game = models.ForeignKey('Game', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wins'
