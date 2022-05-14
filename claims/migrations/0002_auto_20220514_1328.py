# Generated by Django 3.2.13 on 2022-05-14 13:28

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim1',
            name='Q10A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q11A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q12A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q13A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q14A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q15A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q16A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q17A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q18A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q19A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q1A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q20A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q21A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q24A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q25A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q28A',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'Catholic'), (1, 'Christian'), (2, 'Orthodox Jewish'), (3, 'Non-Orthodox Jewish'), (4, 'Buddhist'), (5, 'Mormon'), (6, 'Hindu'), (7, 'Sikh'), (8, 'Atheist'), (9, 'Agnostic'), (10, 'Muslim'), (11, 'Other')], default=None, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q2A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q3A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q4A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q5A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q6A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q7A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q8A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim1',
            name='Q9A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q29A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q30A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q31A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q32A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q33A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q34A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q35A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q36A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q37A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q38A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q39A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q40A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q41A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q42A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q42B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q43A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q44A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q44B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q45A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q46A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q46B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q47A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim2',
            name='Q47B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q48A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q49A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q50A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q51A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q52A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q53A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q54A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q55A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q56A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim3',
            name='Q57A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q58A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q59A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q60A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q61A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q62A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q63A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q64A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q65A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q66A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q67A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q68A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q69A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q70A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q71A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q72A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q73A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q74A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q75A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q76A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q77A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q78A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q78B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q79A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q79B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q80A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q81A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q81B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q82A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q83A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q84A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q85A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q86A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q86B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q87A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q87B',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q88A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim4',
            name='Q89A',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
    ]
