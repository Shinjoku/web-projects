from datetime import date
from django.shortcuts import render, redirect
from .models import Cliente, Empresa, Ordem
from .forms import CadastrarEmpresa, CadastrarCliente, CadastrarOrdem


def index(request):
    ordem_list = Ordem.objects.order_by('id')
    return render(request, 'pros/index.html', {'ordem_list': ordem_list})

# Empresas:-------------------------------------------------------------------------------------------


def empresas(request):
    empresa_list = Empresa.objects.order_by('nome_empresa')
    return render(request, 'pros/empresas.html', {'empresa_list': empresa_list})


def cadastro_empresa(request):
    if request.method == 'POST':
        form = CadastrarEmpresa(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pros:empresas')
        else:
            print('falhou')
    else:
        form = CadastrarEmpresa()
    return render(request, 'pros/cadastro_empresa.html', {'form': form})


def update_empresa(request, pk):
    empresa = Empresa.objects.get(pk=pk)
    form = CadastrarEmpresa(request.POST or None, instance=empresa)
    if form.is_valid():
        form.save()
        return redirect('pros:empresas')
    return render(request, 'pros/update_empresa.html', {'form': form, 'pk': pk})



def delete_empresa(request, pk):
    Empresa.objects.filter(id=pk).delete()
    return redirect('pros:empresas')

# Clientes:--------------------------------------------------------------------------------------------


def clientes(request, empresa_id):
    client_list = Cliente.objects.filter(empresa_id=empresa_id)
    nome_empresa = Empresa.objects.filter(id=empresa_id).get().nome_empresa
    return render(request, 'pros/clientes.html', {'client_list': client_list, 'nome_empresa': nome_empresa,
                                                    'empresa_id': empresa_id})


def cadastro_cliente(request, empresa_id):

    empresa_fk = Empresa.objects.get(id=empresa_id)

    if request.method == 'POST':
        form = CadastrarCliente(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.empresa = empresa_fk
            form.save()
            return redirect('pros:clientes', empresa_id)
        else:
            return redirect('pros:clientes', empresa_id)
    else:
        form = CadastrarCliente()
        nome_empresa = Empresa.objects.filter(id=empresa_id).get().nome_empresa
    return render(request, 'pros/cadastro_cliente.html', {'form': form, 'empresa_id': empresa_id,
                                                             'nome_empresa': nome_empresa})


def delete_cliente(request, empresa_id, pk):
    Cliente.objects.filter(id=pk).delete()
    return redirect('pros:clientes', empresa_id)


def update_cliente(request, empresa_id, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = CadastrarCliente(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('pros:clientes', empresa_id)
    nome_empresa = Empresa.objects.filter(id=empresa_id).get().nome_empresa
    return render(request, 'pros/update_cliente.html', {'form': form, 'empresa_id': empresa_id,
                                                             'nome_empresa': nome_empresa, 'pk': pk})


# Ordens:----------------------------------------------------------------------------------------------

def ordem(request):
    ordem_list = Ordem.objects.order_by('id')
    return render(request, 'pros/index.html', {'ordem_list': ordem_list})


def cadastro_ordem(request):
    empresa_list = Empresa.objects.all()
    client_list = Cliente.objects.all()

    if request.method == 'POST':
        form = CadastrarOrdem(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.cliente = str(request.POST['select2'])
            form.save()
            return redirect('pros:index')
        else:
            print('teste')
    else:
        form = CadastrarOrdem()
    return render(request, 'pros/cadastro_ordem.html', {'form': form, 'client_list': client_list,
                                                        'empresa_list': empresa_list})


def update_ordem(request, pk):
    up_ordem = Ordem.objects.get(id=pk)
    empresa_list = Empresa.objects.all()
    client_list = Cliente.objects.all()
    
    print (up_ordem.id)
    
    form = CadastrarOrdem(request.POST or None, instance=up_ordem)
    if form.is_valid():
        form = form.save(commit=False)
        form.cliente = str(request.POST['select2'])
        form.save()
        return redirect('pros:index')
    return render(request, 'pros/update_ordem.html', {'form': form, 'pk': pk, 'client_list': client_list,
                                                        'empresa_list': empresa_list})


def delete_ordem(request, pk):
    Ordem.objects.filter(id=pk).delete()
    return redirect('pros:index')
