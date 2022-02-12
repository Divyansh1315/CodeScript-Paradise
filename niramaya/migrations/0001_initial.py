# Generated by Django 4.0.1 on 2022-02-11 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=10)),
                ('Level', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('head', models.CharField(max_length=50)),
                ('doctor_nos', models.IntegerField(default=0)),
                ('skilled_nos', models.IntegerField(default=0)),
                ('non_skilled_nos', models.IntegerField(default=0)),
                ('gen_bed', models.IntegerField(default=0)),
                ('spec_bed', models.IntegerField(default=0)),
                ('surg_bed', models.IntegerField(default=0)),
                ('av_gen_bed', models.IntegerField(default=0)),
                ('av_spec_bed', models.IntegerField(default=0)),
                ('av_surg_bed', models.IntegerField(default=0)),
                ('ICU_units', models.IntegerField(default=0)),
                ('CIC_units', models.IntegerField(default=0)),
                ('BIC_units', models.IntegerField(default=0)),
                ('SIC_units', models.IntegerField(default=0)),
                ('PsIC_units', models.IntegerField(default=0)),
                ('PeIC_units', models.IntegerField(default=0)),
                ('NIC_units', models.IntegerField(default=0)),
                ('DIC_units', models.IntegerField(default=0)),
                ('PrIC_units', models.IntegerField(default=0)),
                ('Nursery_units', models.IntegerField(default=0)),
                ('Lab_chem', models.BooleanField(default=False)),
                ('Lab_hemo', models.BooleanField(default=False)),
                ('Lab_microB', models.BooleanField(default=False)),
                ('Lab_trans', models.BooleanField(default=False)),
                ('Lab_immuno', models.BooleanField(default=False)),
                ('Lab_surg_path', models.BooleanField(default=False)),
                ('Lab_cyto', models.BooleanField(default=False)),
                ('C_cath', models.BooleanField(default=False)),
                ('C_rehab', models.BooleanField(default=False)),
                ('C_surgery', models.BooleanField(default=False)),
                ('C_stenting', models.BooleanField(default=False)),
                ('C_intervene', models.BooleanField(default=False)),
                ('C_electro', models.BooleanField(default=False)),
                ('C_vas_interv', models.BooleanField(default=False)),
                ('C_vas_surg', models.BooleanField(default=False)),
                ('R_com_T', models.BooleanField(default=False)),
                ('R_com_TA', models.BooleanField(default=False)),
                ('R_dig_mamo', models.BooleanField(default=False)),
                ('R_dig_IMRT', models.BooleanField(default=False)),
                ('R_dig_MRA', models.BooleanField(default=False)),
                ('R_dig_MRI', models.BooleanField(default=False)),
                ('R_dig_PET', models.BooleanField(default=False)),
                ('R_dig_SPECT', models.BooleanField(default=False)),
                ('Re_phy', models.BooleanField(default=False)),
                ('Re_sp', models.BooleanField(default=False)),
                ('EME_dept', models.BooleanField(default=False)),
                ('EME_ped_TC', models.BooleanField(default=False)),
                ('EME_TC', models.BooleanField(default=False)),
                ('N_EEG', models.BooleanField(default=False)),
                ('N_sleep', models.BooleanField(default=False)),
                ('Sp_BICU', models.BooleanField(default=False)),
                ('Sp_CCU', models.BooleanField(default=False)),
                ('Sp_det', models.BooleanField(default=False)),
                ('Sp_ICU', models.BooleanField(default=False)),
                ('Sp_NIC', models.BooleanField(default=False)),
                ('Sp_PeIC', models.BooleanField(default=False)),
                ('Sp_PrIC', models.BooleanField(default=False)),
                ('Sp_PsIC', models.BooleanField(default=False)),
                ('Sp_SICU', models.BooleanField(default=False)),
                ('Sp_TCU', models.BooleanField(default=False)),
                ('On_chemo', models.BooleanField(default=False)),
                ('On_rad', models.BooleanField(default=False)),
                ('Or_heart', models.BooleanField(default=False)),
                ('Or_intestinal', models.BooleanField(default=False)),
                ('Or_kidney', models.BooleanField(default=False)),
                ('Or_liver', models.BooleanField(default=False)),
                ('Or_lung', models.BooleanField(default=False)),
                ('Or_pancreas', models.BooleanField(default=False)),
                ('ortho_Arth', models.BooleanField(default=False)),
                ('ortho_JR', models.BooleanField(default=False)),
                ('ortho_spine', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]