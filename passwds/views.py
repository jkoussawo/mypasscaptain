from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from passwds.forms import PasswordForm
from passwds.helpers import password_generator

# Create your views here.
def test(request):

    return HttpResponse('index')


def index(request,passwd_gen=''):
    
    if request.method == 'POST':
        form = PasswordForm(request.POST)

        if form.is_valid():
            majuscules = str(form.cleaned_data['majuscules'])
            minuscules = str(form.cleaned_data['minuscules'])
            chiffres = str(form.cleaned_data['chiffres'])
            speciaux = str(form.cleaned_data['speciaux'])
            nbreCaractere = form.cleaned_data['nbreCaractere']
            
            print("{}".format(type(majuscules)))

            print("Debug : {0} - {1} - {2} - {3}".format(majuscules,minuscules,chiffres,speciaux))

            print("Taille : {}".format(nbreCaractere))

            passwd_gen = password_generator(minuscules,majuscules,chiffres,speciaux,nbreCaractere)

            print('mot de passe : {} '.format(passwd_gen))

            #return HttpResponseRedirect('index')
    
    else:
        form = PasswordForm()
        
    content = {
        'date': datetime.now(),
        'form': form,
        'passwd_gen' : passwd_gen 
    }

    return render(request, 'passwds/index.html', content )