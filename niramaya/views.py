import imp
from pickle import NONE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from .models import hospital

# Create your views here.


def index(request):
    # if request.user:
    #     return render(request,'niramaya/index.html',{'username': request.user})
    # else:
    #     return render(request,'nirmaya/index.html')
    return render(request,'niramaya/index.html')

def handelLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User = authenticate(username = username, password = password)

        if User is not None:
            login(request,User)
            print('user logged in successfully')
            return render(request,'niramaya/register.html',{'username': request.user})
        else:
            print("something went wrong")
            return render(request,'niramaya/login.html',{})
    return HttpResponse("404 not found: Not authorised please follow the inWebFrame to navigate through pages only")

def handelLogout(request):
    logout(request)
    print('you have been loged out of account successfully')
    return redirect('login')

def createHospital(request):
    if request.method == 'POST':
        user = request.user()
        hospital_name = request.POST['hospital_name']
        serial = request.POST['brach_serial']
        Level = request.POST['hospital_level']
        address = request.POST['branc_add']
        State = request.POST['brach_state']
        district = request.POST['brach_district']
        phone = request.POST['brach_phone']
        head = request.POST['brach_head']
        doctor_nos = request.POST['brach_doctors']
        skilled_nos = request.POST['brach_skilled']
        non_skilled_nos = request.POST['brach_NonSkilled']
        gen_bed = request.POST['brach_gen_bed']
        spec_bed = request.POST['brach_special_bed']
        surg_bed = request.POST['brach_srg_bed']
        av_gen_bed = request.POST['branch_available_gen_beds']
        av_spec_bed = request.POST['branch_available_spec_beds']
        av_surg_bed = request.POST['branch_available_srg_beds']

        ICU_units = request.POST['branch_ICU']
        CIC_units = request.POST['branch_CIC']
        BIC_units = request.POST['branch_BIC']
        SIC_units = request.POST['branch_SIC']
        PsIC_units = request.POST['branch_PsIC']
        PeIC_units = request.POST['branch_PeIC']
        NIC_units = request.POST['branch_NIC']
        TIC_units = request.POST['branch_TIC']
        DIC_units = request.POST['branch_DIC']
        PrIC_units = request.POST['branch_PrIC']
        Nursery_units = request.POST['branch_Nursery']

        Lab_chem = request.POST['Lab_chem']
        Lab_hemo = request.POST['Lab_hemo']
        Lab_microB = request.POST['Lab_microB']
        Lab_trans = request.POST['Lab_trans']
        Lab_immuno = request.POST['Lab_immuno']
        Lab_surg_path = request.POST['Lab_surg_path']
        Lab_cyto = request.POST['Lab_cyto']

        C_cath = request.POST['C_cath']
        C_rehab = request.POST['C_rehab']
        C_surgery = request.POST['C_surgery']
        C_stenting = request.POST['C_stenting']
        C_intervene = request.POST['C_interve']
        C_electro = request.POST['C_electro']
        C_vas_interv = request.POST['C_vas_interv']
        C_vas_surg = request.POST['C_vas_sur']

        R_com_T = request.POST['R_com_T']
        R_com_TA = request.POST['R_com_TA']
        R_dig_mamo = request.POST['R_dig_mamo']
        R_dig_IMRT = request.POST['R_IMRT']
        R_dig_MRA = request.POST['R_MRA']
        R_dig_MRI = request.POST['R_MRI']
        R_dig_PET = request.POST['R_PET']
        R_dig_SPECT = request.POST['R_SPECT']

        Re_phy = request.POST['Re_phy']
        Re_sp = request.POST['Re_sp']

        EME_dept = request.POST['EME_dept']
        EME_ped_TC = request.POST['EME_ped_TC']
        EME_TC = request.POST['EME_TC']

        N_EEG = request.POST['N_sleep']
        N_sleep = request.POST['N_EEG']

        Sp_BICU = request.POST['Sp_BICU']
        Sp_CCU = request.POST['Sp_CCU']
        Sp_det = request.POST['Sp_det']
        Sp_ICU = request.POST['Sp_ICU']
        Sp_NIC = request.POST['Sp_NIC']
        Sp_PeIC = request.POST['Sp_PeIC']
        Sp_PrIC = request.POST['Sp_PrIC']
        Sp_PsIC = request.POST['Sp_PsIC']
        Sp_SICU = request.POST['Sp_SICU']
        Sp_TCU = request.POST['Sp_TCU']

        On_chemo = request.POST['On_chemo']
        On_rad = request.POST['On_rad']

        Or_heart = request.POST['Or_heart']
        Or_intestinal = request.POST['Or_intestinal']
        Or_kidney = request.POST['Or_kidney']
        Or_liver = request.POST['Or_liver']
        Or_lung = request.POST['Or_lung']
        Or_pancreas = request.POST['Or_pancreas']

        ortho_Arth = request.POST['Ortho_Arth']
        ortho_JR = request.POST['Ortho_JR']
        ortho_spine = request.POST['Ortho_spine']

        hospital = hospital(user=user,hospital_name=hospital_name,serial=serial,Level=Level,address=address,State=State,district=district,phone=phone,head=head,doctor_nos=doctor_nos,skilled_nos=skilled_nos,non_skilled_nos=non_skilled_nos,gen_bed=gen_bed,spec_bed=spec_bed,surg_bed=surg_bed,av_gen_bed=av_gen_bed,av_spec_bed=av_spec_bed,av_surg_bed=av_surg_bed,ICU_units=ICU_units,CIC_units=CIC_units,BIC_units=BIC_units,SIC_units=SIC_units,PsIC_units=PsIC_units,PeIC_units=PeIC_units,NIC_units=NIC_units,TIC_units=TIC_units,DIC_units=DIC_units,PrIC_units=PrIC_units,Nursery_units=Nursery_units,Lab_chem=Lab_chem,Lab_hemo=Lab_hemo,Lab_microB=Lab_microB,Lab_trans=Lab_trans,Lab_immuno=Lab_immuno,Lab_surg_path=Lab_surg_path,Lab_cyto=Lab_cyto,C_cath=C_cath,C_rehab=C_rehab,C_surgery=C_surgery,C_stenting=C_stenting,C_intervene=C_intervene,C_electro=C_electro,C_vas_interv=C_vas_interv,C_vas_surg=C_vas_surg,R_com_T=R_com_T,R_com_TA=R_com_TA,R_dig_mamo=R_dig_mamo,R_dig_IMRT=R_dig_IMRT,R_dig_MRA=R_dig_MRA,R_dig_MRI=R_dig_MRI,R_dig_PET=R_dig_PET,R_dig_SPECT=R_dig_SPECT,Re_phy=Re_phy,Re_sp=Re_sp,EME_dept=EME_dept,EME_ped_TC=EME_ped_TC,EME_TC=EME_TC,N_EEG=N_EEG,N_sleep=N_sleep,Sp_BICU=Sp_BICU,Sp_CCU=Sp_CCU,Sp_det=Sp_det,Sp_ICU=Sp_ICU,Sp_NIC=Sp_NIC,Sp_PeIC=Sp_PeIC,Sp_PrIC=Sp_PrIC,Sp_PsIC=Sp_PsIC,Sp_SICU=Sp_SICU,Sp_TCU=Sp_TCU,On_chemo=On_chemo,On_rad=On_rad,Or_heart=Or_heart,Or_intestinal=Or_intestinal,Or_kidney=Or_kidney,Or_liver=Or_liver,Or_lung=Or_lung,Or_pancreas=Or_pancreas,ortho_Arth=ortho_Arth,ortho_JR=ortho_JR,ortho_spine=ortho_spine)

        hospital.save()

    return render(request,'niramaya/register.html',{'username': request.user})

def refer(request):
    return render(request,'niramaya/ref1.html')

def request(request):
    return render(request,'niramaya/request.html')

def history(request):
    return HttpResponse('referal history')

def account(request):
    return render(request,'niramaya/register.html',{'username': request.user})

def Login(request):
    return render(request,'niramaya./login.html')