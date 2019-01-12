from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from datetime import datetime,timedelta

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.db.models import Sum
from . import models
from django.db.models import  F
from django.contrib.auth.decorators import login_required
from .forms import OrderRegister,AddGet, product_Add,PostForm,new,ItemState1
class TableCreateView(CreateView):
    model = models.Table
    fields = ('table_num',)
    success_url = reverse_lazy('person_changelist')

class TableListView(ListView):
      model = models.Table
      context_object_name = 'people'

def load_Tables(request):

    cities = models.Table.objects.all()
    context={
        'cities': cities
    }
    return render(request,'list.html', context)

def RegisterOrder(request,ln):


    if request.method == 'GET':

        data = OrderRegister
        return render(request, 'reg.html', {'formreg': data,'ln':ln})
    else:


        data = OrderRegister(request.POST)

        if data.is_valid():

            table = models.Order()

            table.table_num_id = data.cleaned_data['table_num']
            table.lan=ln
            table.save()
            #last= models.Order.objects.last()
            last= models.Order.objects.last()
            a=last.id
            context = {
                    'last': last
             }
        return redirect('/list/' +str(a) )


def product(request,Order_id):
       sub2 = get_object_or_404(models.Order, id=Order_id)
       count=models.Get.objects.filter(order_id=Order_id)
       g=count.count()
       lan = sub2.lan

       prod = models.Category.objects.all()
       items = models.Product.objects.filter(category__in=prod)

       #swits = models.Product.objects.filter(Type=3)

       u = request.get_full_path()
       n=0
       context = {
                'products':prod,
                'path': u,'lan':lan,
                'path1': Order_id,
                'items':items,
                'n':n,
                'g':g






       }
       return render(request, 'products.html', context)

def item(request,Order_id,Product_id):

    m=Order_id
    subr = get_object_or_404(models.Order, id=Order_id)
    s = subr.state
    if s == 2:
        return redirect('/')


    if request.method == 'GET':
      sub2 = get_object_or_404(models.Order, id=Order_id)
      lan = sub2.lan

      item = models.Product.objects.get(id=Product_id)
      invoice=models.Get.objects.filter(order_id=Order_id)
      #prodname = models.Product.objects.get(id=invoice.product_id)
      data=AddGet()
      context = {
         'item': item,
          'former':data,
          'invoice':invoice,
          'Order_id': Order_id,
          'lan':lan
      }
      return render(request,'Item.html', context)
    else:

        item = models.Product.objects.get(id=Product_id)
        d=item.Price

        item1 = models.Order.objects.get(id=Order_id)
        data = AddGet(request.POST)

        if data.is_valid():

            table = models.Get()

            table.count = data.cleaned_data['count']
            table.order_id = item1
            table.product_id = item
            c=d*data.cleaned_data['count']
            table.value=c
            table.save()

            f=Order_id

       # context = {
        #           'former': data
        #}

        return redirect('/invoice/' +str(f))


def invoice(request,Order_id):
      msg=''

      sub2 = get_object_or_404(models.Order, id=Order_id)
      lan = sub2.lan
      b=Order_id
      res = models.Get.objects.filter(order_id=Order_id).select_related()
      del1= models.Order.objects.get(id=Order_id)
      d=del1.state
      val= res.aggregate(total=Sum('value'))
      a = (val.get('total'))
      value = models.Order.objects.filter(id=Order_id).update(value=a)
      msg =  'you cannt delete after confirm'
      context = {'res': res,'b':b,'a':a,'lan':lan,'d':d,'msg':msg,
      }

      return render(request,'invoice.html',context)


def delete(request,product_id,Order_id):

    a = Order_id
    order=get_object_or_404(models.Order, id=Order_id)
    am=order.state

    if am != 1:

       post1=models.Get.objects.filter(order_id=Order_id)
       post2=post1.get(id=product_id)
       post2.delete()
    return redirect('/invoice/'+str(a))

def ensure(request,Order_id):
    post = models.Order.objects.filter(id=Order_id).update(state=1)
    pos1 = models.Order.objects.get(id=Order_id)
    pos2 = models.Table.objects.filter(table_num=pos1.table_num_id).update(state=1)


    return redirect('/list/' + str(Order_id))

@login_required
def control(request):
    return render(request,'control.html')

@login_required
def kitchen(request):

       post1 = models.Get.objects.filter(state=0)
       peep=post1.count()
       ln = models.Rest.objects.get(id=2)
       L = ln.Language
       orders=models.Order.objects.filter(state=1)

       d=orders
       prod=models.Get.objects.filter(order_id__in=orders,state=0)

       c= d.count()-1

       data=ItemState1
       context={'orders':orders,'prod':prod,'L':L,
             'peep':peep,'form': data}

       return render(request,'kitchen.html',context)


       return redirect('/kitchen/')


@login_required
def order_control(request):
    ln=models.Rest.objects.get(id=2)
    L=ln.Language
    orders=models.Order.objects.filter(state=1)

    d=orders
    prod=models.Get.objects.filter(order_id__in=orders)

    c= d.count()-1

    context={'orders':orders,'prod':prod,'L':L}

    return render(request,'order_control.html',context)


def done(request,order_id):

    post2=models.Get.objects.filter(order_id=order_id)

    post2.delete()
    post = models.Order.objects.filter(id=order_id).update(state=2)
    post1 = models.Order.objects.get(id=order_id)
    post3 = models.Table.objects.filter(table_num=post1.table_num_id).update(state=0)

    a = post1.value
    b=post1.date


    test = models.accounts.objects.filter(date=b)
    s=test.count()
    if s==0:
      p = models.accounts(date=b,value=a)
      p.save()
    else:
      up=models.accounts.objects.filter(date=b).update(value=F('value')+a)


    return redirect('/order_control/')


def print(request,order_id):
    post1 = models.Get.objects.filter(order_id=order_id).select_related()
    inf=models.Rest.objects.get(id=2)
    L = inf.Language
    ord=models.Order.objects.get(id=order_id)

    return render(request,'print.html',{'print':post1,'L':L,'ord':ord,'inf':inf})


def donek(request,id):
    post1 = models.Get.objects.filter(id=id).update(state=1)
    return redirect('/kitchen/')
def ItemState(request,name):
    post1 = models.Product.objects.filter(name=name).update(state=0)
    return redirect('/kitchen/')



def productRegistration(request):
   prod = product_Add(request.POST or None,request.FILES or None)
   if prod.is_valid():
       ins = prod.save(commit=False)
       ins.save()

   return render(request,'prodRegester.html',{'form': prod})


def Rest(request):
    cities = models.Rest.objects.all()
    context = {
        'cities': cities
    }
    return render(request, 'base.html', context)

def Rest_infor(request):

       form = PostForm(request.POST or None,request.FILES or None)
       if form.is_valid():
          ins=form.save(commit=False)
          ins.save()


       return render(request, 'Rest_inform.html', {'form': form})




def start(request,ln):
    msg=''
    inform = models.Rest.objects.all()
    if request.method == 'GET':

       form = new(request.POST or None)
       context = {
          'form': form,
          'inform':inform,
           'ln':ln,
       }
       return render(request,'start.html',context)
    else:
        form = new(request.POST or None)
        if form.is_valid():
          a= form.cleaned_data['order']
          b= form.cleaned_data['table']
          fil=models.Order.objects.filter(id=a)
          m = fil.count()
          if m ==0 :
              msg =  'Given information is valid ,Try again'

              context = {'form': form,
                         'inform': inform,
                  'msg': msg}
              return render(request, 'start.html', context)
          else:
              sub =get_object_or_404(models.Order, id=a)

              c=sub.table_num_id
              s=sub.state
              if s==2:
                  return redirect('/')

              if str(c) == str(b):

                 return redirect('/list/' + str(a))
              else:
                 msg = 'Given information is valid ,Try again'

                 context = {
                   'msg': msg}
                 return render(request, 'start.html', context)

def home(reqest):
    return render(reqest,'home.html')

@login_required
def cash(request):
    res = models.Order.objects.filter(state=2)
    val = res.aggregate(total=Sum('value'))


    context={'res':res,'val':val}
    return render(request,'cash.html',context)
