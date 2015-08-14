#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse as r
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from django.contrib.auth.models import Group
from usuarios.forms import UsuarioForm,UsuarioFormEditar,FormAlterarSenha


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.views import group_required,verifica_membro

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import hashlib

#@login_required
#@group_required('Administrador')
def usuarios(request):
	'''
	  @usuarios: view para listar os usuarios cadastrados no sistema 
	'''
	usuarios = Usuario.objects.all().order_by('first_name')

	return render(request, 'usuarios.html',{'usuarios': usuarios})

#@login_required
#@group_required('Administrador')
def usuario_novo(request):
	'''
	  @usuario_novo: Metodo de criação de um novo Usuario 
	'''
	form = UsuarioForm()
	
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
	
		if form.is_valid():
			usuario = form.save(commit=False)
			usuario.save()

			# Criando o Hashcode do Usuario
			usuario.hashcode  = hashlib.md5(str(usuario.id)).hexdigest()
			usuario.password_textplan= usuario.password
			# Password criptografado
			usuario.set_password(usuario.password)
			#adicionando usuario a staff para permitir upload de fotos no ckeditor
			usuario.is_staff = True

			grupo = Group.objects.get(id=request.POST['grupo'])
			usuario.groups.add(grupo) 
			usuario.save()
			
			return HttpResponseRedirect( r('usuarios:usuarios'))
		else:  
			return render(request,'usuario_novo.html',{'form': form,'status':'Novo'})
	else:
		return render(request,'usuario_novo.html',{'form': form,'status':'Novo'})


#@login_required
#@group_required('Administrador')
def usuario_editar(request,usuario_id):
	'''
	  @usuario_editar: Metodo de edição de um usuario cadastrado na base
	'''
	pessoa = Usuario.objects.get(id=usuario_id)
	grupos_adicionados = pessoa.groups.all()
	form = UsuarioFormEditar(instance=pessoa)
	
	if request.method == 'POST':
		form = UsuarioFormEditar(request.POST,instance=pessoa)
		
		if form.is_valid():            
			usuario = form.save(commit=False)
			grupo = Group.objects.get(id=request.POST['grupo'])
			usuario.groups.clear()
			usuario.groups.add(grupo) 
			usuario.save()
			
			return HttpResponseRedirect( r('usuarios:usuarios'))
		else :
			return render(request, 'usuario_novo.html', { 'form':form ,'status':'Editar','id_usuario':usuario_id})
	else:           
		return render(request,'usuario_novo.html',{'form': form,'status':'Editar','id_usuario':usuario_id})


@login_required
@group_required('Administrador')
def usuario_alterar_status(request,usuario_id):
	'''
	  @usuario_alterar_status: View para alterar status de um usuário
	'''
	# Procurando o usuário na base de dados
	usuario = Usuario.objects.get(id=usuario_id)

	if usuario.is_active == True:
		usuario.is_active = False
	else:
		usuario.is_active = True

	usuario.save()

	return HttpResponseRedirect( r('usuarios:usuarios'))

@login_required
def alterar_senha(request):
	'''
	  @alterar_senha: Metodo para alteração de senha de um usuario Pré-cadastrado
	'''
	
	senha_alterada = False 
	
	if request.method == 'POST':
		formSenha = FormAlterarSenha(request.POST)
		if formSenha.is_valid():
			# Obtendo dados do request
			password = request.POST.get('password1')
			
			# Procurando o usuario na base de dados
			usuario = Usuario.objects.get(id=request.user.id)
			
			# Salvando o usuario
			usuario.password_textplan=password
			# Alterando a senha do usuario
			usuario.set_password(password)            
			
			usuario.save()

			senha_alterada = True
			
			return render(request,'alterar_senha.html',{'form': formSenha,'senha_alterada':senha_alterada})
		else:
			return render(request,'alterar_senha.html',{'form': formSenha,'senha_alterada':senha_alterada})
	else:
		return render(request,'alterar_senha.html',{'form': FormAlterarSenha(),'senha_alterada':senha_alterada})

def esqueci_senha(request):
	'''
	  @esqueci_senha: Metodo para recuperar a senha do usuario
	'''    
	erro = False

	if request.method == 'POST':
		# Pegando o CPF do POST
		email = request.POST.get('email')
		
		# Procurando um usuario na base com o email enviado
		try:
			usuario = Usuario.objects.get(email=email)
			
			# Envia email para o usuario informando a senha
			email_recuperar_senha(request,usuario.id)

			enviado = True

			return render(request,'esqueci_senha.html',{'usuario':usuario,'enviado':enviado})
		except:
			erro = True
			return render(request,'esqueci_senha.html',{'erro':erro,'email':email})        
	else:           
		return render(request,'esqueci_senha.html')

def recuperar_senha(request,usuario_hash):
	'''
	  @recuperar_senha: Metodo para recuperar a senha do usuario
	'''
	# Procurando o usuario na base de dados
	usuario = Usuario.objects.get(hashcode=usuario_hash)
	erro = False

	if request.method == 'POST':
		# Pegando o CPF do POST
		cpf = request.POST.get('cpf').replace('.','').replace('-','').strip()
		if usuario.cpf == cpf:

			# Envia email para o usuario informando a senha
			email_reenviar_senha(request,usuario.id)

			# Colocando o Status na sessão
			request.session['recuperar_senha'] = {'enviado':True}

			return HttpResponseRedirect( r('login'))
		else:
			erro = True
			return render(request,'recuperar_senha.html',{'usuario':usuario,'erro':erro})        
	else:           
		return render(request,'recuperar_senha.html',{'usuario':usuario})

def email_recuperar_senha(request, usuario_id):
	'''
		@envia_email_ativacao: Função para envio de email para o cliente ativar a sua conta
	'''

	configuracao = ConfiguracaoGeral.objects.get(id=1)
	
	usuario = Usuario.objects.get(id=usuario_id)
	
	link_dominio = "http://%s" % request.META['HTTP_HOST']

	# Cabeçalho do email
	assunto, from_email, to_email = 'Recuperar Senha', configuracao.email, usuario.email


	# Conteudo HTML
	html_conteudo = render_to_string('email/email_recuperar_senha.html',{'usuario':usuario,'configuracao':configuracao,'link_dominio':link_dominio}) 

	# Remover as Tags HTML para ficar somente o texto
	text_conteudo = render_to_string('email/email_recuperar_senha.txt',{'usuario':usuario,'configuracao':configuracao,'link_dominio':link_dominio}) 
	
	# Cria o email e anexa a versão HTML
	msg = EmailMultiAlternatives(assunto, text_conteudo, from_email, [to_email])

	msg.attach_alternative(html_conteudo, "text/html")
	msg.send()

	return True

def email_reenviar_senha(request, usuario_id):
	'''
		@email_reenviar_senha: Função para envio de email para o usuario com a sua senha
	'''
	configuracao = ConfiguracaoGeral.objects.get(id=1)

	usuario = Usuario.objects.get(id=usuario_id)

	link_dominio = "http://%s" % request.META['HTTP_HOST']
	
	# Cabeçalho do email
	assunto, from_email, to_email = 'Recuperar Senha', configuracao.email, usuario.email

	# Conteudo HTML
	html_conteudo = render_to_string('email/email_reenviar_senha.html',{'usuario':usuario,'configuracao':configuracao,'link_dominio':link_dominio}) 

	# Remover as Tags HTML para ficar somente o texto
	text_conteudo = render_to_string('email/email_reenviar_senha.txt',{'usuario':usuario,'configuracao':configuracao,'link_dominio':link_dominio}) 

	# Cria o email e anexa a versão HTML
	msg = EmailMultiAlternatives(assunto, text_conteudo, from_email, [to_email])
	msg.attach_alternative(html_conteudo, "text/html")
	msg.send()

	return True