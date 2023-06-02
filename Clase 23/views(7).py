from typing import List

from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserRegisterForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required




# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)

@login_required
def inicio(request):

      return render(request, "AppCoder/inicio.html")



def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["camada"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)



def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al menú
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})




class CursoList(ListView):

      model = Curso 
      template_name = "AppCoder/cursos_list.html"



class CursoDetalle(DetailView):

      model = Curso
      template_name = "AppCoder/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/AppCoder/curso/list"




def logout_request(request):
      logout(request)
      messages.info(request, "Saliste sin problemas")
      return redirect("inicio")
     

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppCoder/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})