# Generated by Django 3.0 on 2020-05-05 06:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=200, null=True)),
                ('job', models.IntegerField(choices=[(1, 'ケアマネ'), (2, '病院SW'), (3, '病院看護師'), (4, '病院医師'), (5, 'クリニックSW'), (6, 'クリニック看護師'), (7, 'クリニック医師'), (8, '訪問介護士'), (9, '施設介護士'), (10, '患者さん'), (11, '患者さんご家族')])),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('attribute', models.IntegerField(choices=[(1, '在宅クリニック'), (2, '居宅介護支援'), (3, '訪問看護ST'), (4, '急性期病院'), (5, '緩和ケア病棟'), (6, '在宅療養支援病院'), (7, '外来クリニック'), (8, '歯科クリニック'), (9, 'グループホーム'), (10, '介護付有料'), (11, '住宅型有料'), (12, 'サ高住'), (13, '小規模多機能'), (14, '特養'), (15, '老健'), (16, '他の施設'), (17, '訪問介護'), (18, '訪問入浴'), (19, '定期巡回'), (20, 'デイサービス'), (21, 'ショートステイ')])),
                ('address', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=200, null=True)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributes', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Service')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='attr',
            field=models.ManyToManyField(to='hello.ServiceAttr'),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referrer_name', models.CharField(default='', help_text='あなた様のお名前', max_length=30, verbose_name='ご依頼者')),
                ('attribute', models.IntegerField(choices=[(1, 'ケアマネ'), (2, '病院SW'), (3, '訪問看護師'), (4, '病院看護師'), (5, 'ご家族')], default=5, help_text='患者様とのご関係', verbose_name='ご関係')),
                ('phone', models.IntegerField(default='', help_text='連絡のとれる電話番号', verbose_name='電話番号')),
                ('patient_name', models.CharField(default='', help_text='患者様のお名前', max_length=30, verbose_name='患者様')),
                ('birthday', models.DateField(default='', help_text='患者様の生年月日 例：「1977-10-30」', verbose_name='生年月日')),
                ('gender', models.IntegerField(choices=[(1, '女性'), (2, '男性')], default=1, verbose_name='性別')),
                ('purpose', models.IntegerField(choices=[(1, '医療的介護'), (2, '身体介護'), (3, '認知症介護'), (4, '生活介護'), (5, 'ターミナルケア'), (6, '新型コロナ感染疑い')], default=6, help_text='一つを選択', verbose_name='ご病状')),
                ('address', models.CharField(default='', help_text='例:「札幌市中央区南1条東2丁目8-1」', max_length=100, verbose_name='住所')),
                ('comment', models.TextField(blank=True, default='', help_text='必要あればなんでもご記載ください。', max_length=500, verbose_name='コメント')),
                ('file', models.ImageField(blank=True, default='', upload_to='media/', verbose_name='保険証・薬情報')),
                ('need', models.ManyToManyField(to='hello.PatientNeed')),
            ],
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.IntegerField(default=0)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('start_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Friend')),
            ],
        ),
    ]
