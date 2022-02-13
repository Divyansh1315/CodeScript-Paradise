from datetime import datetime
from email.policy import default
from pyexpat import model
from sre_parse import State
from urllib import request
from django import forms
from django.db import models
from django.contrib.auth.models import User

class hospital(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sno = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100)
    serial = models.CharField(max_length=10,unique=True)
    Level = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    State = models.CharField(max_length=50)
    district = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    head = models.CharField(max_length=50)
    doctor_nos = models.IntegerField(default=0)
    skilled_nos = models.IntegerField(default=0)
    non_skilled_nos = models.IntegerField(default=0)
    gen_bed = models.IntegerField(default=0)
    spec_bed = models.IntegerField(default=0)
    surg_bed = models.IntegerField(default=0)
    av_gen_bed = models.BooleanField(default=False)
    av_spec_bed = models.BooleanField(default=False)
    av_surg_bed = models.BooleanField(default=False)
    ICU_units = models.BooleanField(default=False)
    CIC_units = models.BooleanField(default=False)
    BIC_units = models.BooleanField(default=False)
    SIC_units = models.BooleanField(default=False)
    PsIC_units = models.BooleanField(default=False)
    PeIC_units = models.BooleanField(default=False)
    NIC_units = models.BooleanField(default=False)
    DIC_units = models.BooleanField(default=False)
    PrIC_units = models.BooleanField(default=False)
    Nursery_units = models.BooleanField(default=False)

    Lab_chem = models.BooleanField(default=False)
    Lab_hemo = models.BooleanField(default=False)
    Lab_microB = models.BooleanField(default=False)
    Lab_trans = models.BooleanField(default=False)
    Lab_immuno = models.BooleanField(default=False)
    Lab_surg_path = models.BooleanField(default=False)
    Lab_cyto = models.BooleanField(default=False)

    C_cath = models.BooleanField(default=False)
    C_rehab = models.BooleanField(default=False)
    C_surgery = models.BooleanField(default=False)
    C_stenting = models.BooleanField(default=False)
    C_intervene = models.BooleanField(default=False)
    C_electro = models.BooleanField(default=False)
    C_vas_interv = models.BooleanField(default=False)
    C_vas_surg  = models.BooleanField(default=False)

    R_com_T  = models.BooleanField(default=False)
    R_com_TA  = models.BooleanField(default=False)
    R_dig_mamo  = models.BooleanField(default=False)
    R_dig_IMRT  = models.BooleanField(default=False)
    R_dig_MRA  = models.BooleanField(default=False)
    R_dig_MRI  = models.BooleanField(default=False)
    R_dig_PET  = models.BooleanField(default=False)
    R_dig_SPECT  = models.BooleanField(default=False)

    Re_phy  = models.BooleanField(default=False)
    Re_sp  = models.BooleanField(default=False)

    EME_dept  = models.BooleanField(default=False)
    EME_ped_TC  = models.BooleanField(default=False)
    EME_TC  = models.BooleanField(default=False)

    N_EEG  = models.BooleanField(default=False)
    N_sleep  = models.BooleanField(default=False)
    Sp_BICU  = models.BooleanField(default=False)
    Sp_CCU  = models.BooleanField(default=False)
    Sp_det  = models.BooleanField(default=False)
    Sp_ICU  = models.BooleanField(default=False)
    Sp_NIC  = models.BooleanField(default=False)
    Sp_PeIC  = models.BooleanField(default=False)
    Sp_PrIC  = models.BooleanField(default=False)
    Sp_PsIC  = models.BooleanField(default=False)
    Sp_SICU  = models.BooleanField(default=False)
    Sp_TCU  = models.BooleanField(default=False)

    On_chemo  = models.BooleanField(default=False)
    On_rad  = models.BooleanField(default=False)

    Or_heart  = models.BooleanField(default=False)
    Or_intestinal  = models.BooleanField(default=False)
    Or_kidney  = models.BooleanField(default=False)
    Or_liver  = models.BooleanField(default=False)
    Or_lung  = models.BooleanField(default=False)
    Or_pancreas  = models.BooleanField(default=False)

    ortho_Arth  = models.BooleanField(default=False)
    ortho_JR  = models.BooleanField(default=False)
    ortho_spine  = models.BooleanField(default=False)

    def __str__(self):
        return   self.hospital_name +  ' @ ' + ' | ' + self.district + ' | ' + self.State 
    



class refernce(models.Model):
    refernce_sno = models.AutoField(primary_key=True)
    refernce_date = models.DateTimeField(default=datetime.now,blank=True)
    refernce_hospital = models.ForeignKey(hospital,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    patientName = models.CharField(max_length=50,default='default')
    patientID = models.CharField(max_length=20)
    patientInfo = models.FileField(upload_to='documents/')
    message = models.CharField(max_length=500)
    acceptance_choices =[
    (1, "Waiting"),
    (2, "Accepted"),
    (3, "Rejected"),
]
    acceptance = models.CharField(choices=acceptance_choices ,default=1,max_length=2)

    def __str__(self):
        return ' from ' + self.user.username + ' for '  + self.patientName +'|  message:  ' + self.message
# Create your models here.
