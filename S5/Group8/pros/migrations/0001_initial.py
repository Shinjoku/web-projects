# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitante', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=100)),
                ('cargo', models.CharField(blank=True, max_length=100)),
                ('tel', models.CharField(max_length=50)),
                ('ramal', models.CharField(max_length=50)),
                ('cel', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=200)),
                ('nome_social', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=20, unique=True)),
                ('insc_estadual', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=300)),
                ('cep', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50)),
                ('num_nf_entrada', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=512)),
                ('acessorios', models.CharField(max_length=200)),
                ('observacoes', models.CharField(max_length=200)),
                ('data_envio_orcamento', models.CharField(max_length=12)),
                ('data_aprovacao', models.CharField(max_length=12)),
                ('num_pedido', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('executante', models.CharField(max_length=100)),
                ('data_liberacao', models.CharField(max_length=12)),
                ('num_nf_servico', models.CharField(max_length=20)),
                ('num_nf_vendas', models.CharField(max_length=20)),
                ('num_nf_devolucao', models.CharField(max_length=20)),
                ('responsavel_preenchimento', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pros.Empresa'),
        ),
    ]
