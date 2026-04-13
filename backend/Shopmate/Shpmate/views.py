import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from Shpmate.models import *


def login_add(request):
    return render(request,'index.html')

def login_post(request):
    uname = request.POST['uname']
    psw = request.POST['psw']

    d = login.objects.filter(username=uname,password=psw)

    if d.exists():
        logindata = d[0]
        request.session['lid']=logindata.id
        request.session['lin']="lg"


        if logindata.usertype == 'admin':
            return redirect('/adminhome')
        elif logindata.usertype == 'shop':
            return redirect('/ShopHome')
        else:
            return HttpResponse("<script>alert('Invalid role');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('login failed');window.location='/'</script>")

def logout(request):
    request.session['lin']=''
    return HttpResponse("<script>alert('logout');window.location='/'</script>")

def forgetpassword(request):
    return render(request,'forgetpassword.html')

def forgotpassword_post(request):
    Email = request.POST['email']
    d=login.objects.filter(username=Email)
    if d.exists():
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("abhinavmohan778@gmail.com", "higo xdna uwjq klyz")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "abhinavmohan778@gmail.com"
        msg['To'] = d[0].username
        msg['Subject'] = "Forgeted Password"
        body = "Your Password is:- - " + str(d[0].password)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("<script>alert('password send successfully');window.location='/'</script>")

    else:
        return HttpResponse("<script>alert('password not sended');window.location='/'</script>")


#admin module
def adminhome(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request,'Admin/index.html')

def Changepswadmin(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request,'Admin/ChangePassword.html')

def Changepsw_post(request):
    cpsw = request.POST['cpsw']
    npsw = request.POST['npsw']
    copsw = request.POST['copsw']
    usertype = 'admin'


    psw=   login.objects.filter(password=cpsw,id=request.session['lid'])
    if psw.exists():
        if npsw==copsw:
            login.objects.filter(id=request.session['lid']).update(password=npsw)
            return HttpResponse("<script>alert('Changed Successfully');window.location='/'</script>")
        return HttpResponse("<script>alert('password missmatched');window.location='/'</script>")
    return HttpResponse("<script>alert('Wrong current password');window.location='/'</script>")


def Viewshop(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Shop.objects.filter(LOGIN__usertype='pending')
    return render(request,'Admin/viewandverifyshop.html',{'view':data})

def approveshop(request,id):
    l=login.objects.filter(id=id).update(usertype='shop')
    lm = login.objects.filter(id=id)
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("abhinavmohan778@gmail.com", "higo xdna uwjq klyz")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "abhinavmohan778@gmail.com"
    msg['To'] = lm[0].username
    msg['Subject'] = "Approoved your Request"
    body = "Your Password is:- - " + str(lm[0].password)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Approved');window.location='/Viewshop'</script>")

def rejectshop(request,id):
    login.objects.filter(id=id).update(usertype='reject')
    lm = login.objects.filter(id=id)
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("abhinavmohan778@gmail.com", "higo xdna uwjq klyz")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "abhinavmohan778@gmail.com"
    msg['To'] = lm[0].username
    msg['Subject'] = "Rejected your Request"
    body = "Your Appliction Rejcted"
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Approved');window.location='/Viewshop'</script>")

def verifiedshop(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Shop.objects.filter(LOGIN__usertype='shop')
    return render(request,'Admin/verifiedshops.html',{'view':data})

def viewuser(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = User.objects.all()
    return render(request,'Admin/Viewuser.html',{'view':data})

def viewcomplaints(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Complaints.objects.all()
    return render(request,'Admin/ViewComplaints.html',{'view':data})

def viewfeedback(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = feedback.objects.all()
    return render(request,'Admin/viewfeedback.html',{'view':data})


def Addcategorey(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'Admin/addcategorey.html')

def addcategorey_post(request):
    name = request.POST['cat']

    if categorey.objects.filter(Name=name).exists():
        return HttpResponse("<script>alert('Already Exist');window.location='/Addcategorey'</script>")

    obj = categorey()
    obj.Name = name
    obj.save()

    return HttpResponse("<script>alert('Added');window.location='/viewcategorey'</script>")

def viewcategorey(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = categorey.objects.all()
    return render(request,'Admin/viewCategorey.html',{'view':data})

def editcate(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = categorey.objects.get(id=id)
    return render(request,'Admin/editcategorey.html',{"views":data})

def editcat_p(request,id):
    name = request.POST['cat']
    if categorey.objects.filter(Name=name).exists():
        return HttpResponse("<script>alert('Already Exist');window.location='/viewcategorey'</script>")

    categorey.objects.filter(id=id).update(Name=name)
    return HttpResponse("<script>alert('Edited');window.location='/viewcategorey'</script>")

def delcate(request,id):
    categorey.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/viewcategorey'</script>")

def sndreplay(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'Admin/sndreplay.html',{"id":id})

def sndreplay_p(request,id):
    Sreplay = request.POST['rel']
    rdate = request.POST['rdate']

    Complaints.objects.filter(id=id).update(replay=Sreplay,replay_date=rdate)
    return HttpResponse("<script>alert('Sended Successfully');window.location='/viewcomplaints'</script>")

#Shop Module
def ShopHome(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request,'Shop/index.html')

def Changepswshop(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request,'Shop/ChangePassword.html')

def Changepsw_posts(request):
    cpsw = request.POST['cpsw']
    npsw = request.POST['npsw']
    copsw = request.POST['copsw']
    usertype = 'shop'


    psw=   login.objects.filter(password=cpsw,id=request.session['lid'])
    if psw.exists():
        if npsw==copsw:
            login.objects.filter(id=request.session['lid']).update(password=npsw)
            return HttpResponse("<script>alert('Changed Successfully');window.location='/'</script>")
        return HttpResponse("<script>alert('password missmatched');window.location='/'</script>")
    return HttpResponse("<script>alert('Wrong current password');window.location='/'</script>")


def RegisterShop(request):
    return render(request,'Shop/RegisterShop.html')

def Regshop_post(request):
    sname = request.POST['sname']
    email = request.POST['email']
    phn = request.POST['phone']
    latti = request.POST['loc']
    log = request.POST['log']
    oname = request.POST['oname']
    image = request.FILES['img']
    place = request.POST['place']
    uname = request.POST['uname']
    psw = request.POST['psw']

    if Shop.objects.filter(Sname=sname).exists() or Shop.objects.filter(Email=email).exists() or Shop.objects.filter(
            phone=phn).exists():
        return HttpResponse("<script>alert('Already Exist');window.location='/RegisterShop'</script>")
    else:
         #return HttpResponse("<script>alert('Add Diffrent Data');window.location='/RegisterShop'</script>")

        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fs.save(r"C:\Users\Abhinav Mohan\PycharmProjects\Shopmate\Shpmate\Static\Image\\" + d + '.jpg', image)
        path = "/Static/Image/"+d+'.jpg'

        ob=login()
        ob.username=uname
        ob.password=psw
        ob.usertype = 'pending'
        ob.save()

        obj=Shop()
        obj.Sname=sname
        obj.Email=email
        obj.phone=phn
        obj.lattitude=latti
        obj.lognitude=log
        obj.Ownername=oname
        obj.Place=place
        obj.Image=path
        obj.LOGIN=ob
        obj.save()

        return HttpResponse("<script>alert('Added');window.location='/'</script>")


def editshop(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Shop.objects.get(id=id)
    return render(request,'Shop/Editprofile.html',{'view':data})

def editshop_post(request,id):
    try:
        sname = request.POST['sname']
        email = request.POST['email']
        phn = request.POST['phone']
        latti = request.POST['loc']
        oname = request.POST['oname']
        image = request.FILES['img']
        place = request.POST['place']


        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fs.save(r"C:\Users\Abhinav Mohan\PycharmProjects\Shopmate\Shpmate\Static\Image\\" + d + '.jpg', image)
        path = "/Static/Image/" + d + '.jpg'

        Shop.objects.filter(id=id).update(Sname=sname,Email=email,phone=phn,lattitude=latti,Ownername=oname,Image=path,Place=place)
        return HttpResponse("<script>alert('Edited');window.location='/Viewprofileshop'</script>")

    except Exception as e:
        sname = request.POST['sname']
        email = request.POST['email']
        phn = request.POST['phone']
        latti = request.POST['loc']
        oname = request.POST['oname']
        place = request.POST['place']
        Shop.objects.filter(id=id).update(Sname=sname,Email=email,phone=phn,lattitude=latti,Ownername=oname,Place=place)
        return HttpResponse("<script>alert('Edited');window.location='/Viewprofileshop'</script>")

def Viewprofileshop(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Shop.objects.filter(LOGIN=request.session['lid'])
    return render(request,'Shop/viewprofile.html',{'view':data})

def viewcatefories(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = categorey.objects.all()
    return render(request,'Shop/View Categorey.html',{'view':data})

def addpro(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = categorey.objects.all()
    print(data)
    return render(request,'Shop/Add Product.html',{'view':data})

def addpro_post(request):
    pname = request.POST['pname']
    pdate = request.POST['pdate']
    mdate = request.POST['mdate']
    price = request.POST['price']
    cname = request.POST['cname']
    stock = request.POST['stock']
    image = request.FILES['img']

    if Product.objects.filter(Pname=pname).exists():
        return HttpResponse("<script>alert('Already Exist');window.location='/addpro'</script>")
    else:


        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fs.save(r"C:\Users\Abhinav Mohan\PycharmProjects\Shopmate\Shpmate\Static\Image\\" + d + '.jpg', image)
        path = "/Static/Image/" + d + '.jpg'



        obj = Product()
        obj.Pname = pname
        obj.Purchase_date = pdate
        obj.Man_date = mdate
        obj.Price = price
        obj.Image = path
        obj.Stock = stock
        obj.CATEGOREY_id = cname
        obj.SHOP = Shop.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Added');window.location='/Viewproduct'</script>")

def Viewproduct(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Product.objects.filter(SHOP__LOGIN=request.session['lid'])
    return render(request,'Shop/viewproduct.html',{'view':data})

def editpro(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Product.objects.get(id=id)
    d = categorey.objects.all()
    return render(request,'Shop/Editproduct.html',{'view':data ,'see':d})

def editpro_post(request,id):
    try:
        pname = request.POST['pname']
        pdate = request.POST['pdate']
        mdate = request.POST['mdate']
        price = request.POST['price']
        image = request.FILES['img']
        stock = request.POST['stock']
        cname = request.POST['cname']



        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fs.save(r"C:\Users\Abhinav Mohan\PycharmProjects\Shopmate\Shpmate\Static\Image\\" + d + '.jpg', image)
        path = "/Static/Image/" + d + '.jpg'

        Product.objects.filter(id=id).update(Pname=pname, Purchase_date=pdate, Man_date=mdate, Price=price,Image=path,Stock = stock, CATEGOREY_id=cname)
        return HttpResponse("<script>alert('Edited');window.location='/Viewproduct'</script>")

    except Exception as e:
        pname = request.POST['pname']
        pdate = request.POST['pdate']
        mdate = request.POST['mdate']
        price = request.POST['price']
        stock = request.POST['stock']
        cname = request.POST['cname']


        Product.objects.filter(id=id).update(Pname=pname, Purchase_date=pdate, Man_date=mdate, Price=price,Stock = stock, CATEGOREY_id=cname)
        return HttpResponse("<script>alert('Edited');window.location='/Viewproduct'</script>")


def deletepro(request,id):
    Product.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/Viewproduct'</script>")

def viewreviews(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Review.objects.filter(SHOP__LOGIN=request.session['lid'])
    return render(request,'Shop/viewreview.html',{'view':data})

def viewOrder(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Order.objects.filter(SHOP__LOGIN=request.session['lid'])
    return render(request,'Shop/Vieworder.html',{'view':data})

def viewsuborder(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = Order_sub.objects.filter(PRODUCT__SHOP__LOGIN=request.session['lid'],ORDER=id)
    return render(request, 'Shop/ordersub.html', {'view': data})

def updatestatus(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request,'Shop/updatedeliverystatus.html',{'id':id})

def update_post(request,id):
    status = request.POST['status']
    Order.objects.filter(id=id).update(Status=status)
    return HttpResponse("<script>alert('Updated');window.location='/viewOrder'</script>")

#user Module

def Ipaddress(request):
    return JsonResponse

def UserHome(request):
    return JsonResponse

def login_addu(request):
    id = request.POST['lid']
    print(id,"ll")
    uname = request.POST['uname']
    password = request.POST['password']

    d = login.objects.filter(username=uname,password=password)

    if d.exists():
        logindata = d[0]
        lid=d[0].id
        print(lid,"hh")
        if logindata.usertype == 'user':
            return JsonResponse({'status':'ok',"lid":lid})
        else:
            return JsonResponse({'status':'null'})
    else:
        return JsonResponse({'status':'failed'})




def registeruser(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    dob = request.POST['dob']
    image = request.FILES['pic']
    print(image)
    uname = request.POST['uname']
    password = request.POST['password']

    if User.objects.filter(Uname=name).exists() or User.objects.filter(Email=email).exists() or User.objects.filter(Phone=phone).exists() or User.objects.filter(Dob=dob).exists() or login.objects.filter(username=uname).exists():
        return JsonResponse({"status": "no"})

    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    fs.save(r"C:\Users\Abhinav Mohan\PycharmProjects\Shopmate\Shpmate\Static\Image\\" + d + '.jpg', image)
    path = "/Static/Image/" + d + '.jpg'

    ob = login()
    ob.username = uname
    ob.password = password
    ob.usertype = 'user'
    ob.save()


    obj = User()
    obj.Uname = name
    obj.Email = email
    obj.Phone = phone
    obj.Place = place
    obj.post = post
    obj.pin = pin
    obj.Dob = dob
    obj.Image = path
    obj.LOGIN = ob
    obj.save()

    return JsonResponse({'status': 'ok'})

def viewuprofile(request):
    id = request.POST['lid']
    data = User.objects.get(LOGIN=id)
    return JsonResponse({'status': 'ok', 'uname': data.Uname,'email': data.Email,'phone': data.Phone,'place': data.Place,'post': data.post,'pin': data.pin, 'dob': data.Dob,'pic':data.Image,})

def Editprou(request):
    id=request.POST['lid']
    data = User.objects.get(LOGIN=id)

    return JsonResponse({'status':'ok','name':data.Uname,'email':data.Email,'phone':data.Phone,'place':data.Place,'post':data.post,'pin':data.pin,'dob':data.Dob,'pic':data.Image})

def Editu_post(request):
    try:
        id = request.POST['lid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        dob = request.POST['dob']
        image = request.FILES['pic']

        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fs.save(r"C:\Users\Abhinav Mohan\PycharmProjects\Shopmate\Shpmate\Static\Image\\" + d + '.jpg', image)
        path = "/Static/Image/" + d + '.jpg'

        User.objects.filter(LOGIN=id).update(Uname=name, Email=email, Phone=phone, Place=place, post=post, pin=pin,Dob=dob,Image=path)
        return JsonResponse({'status': 'ok'})
    except Exception as e:
        id = request.POST['lid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        dob = request.POST['dob']

        User.objects.filter(LOGIN=id).update(Uname=name, Email=email, Phone=phone, Place=place, post=post, pin=pin,Dob=dob)
        return JsonResponse({'status': 'ok'})


def viewcategoriesu(request):
    data = categorey.objects.all()
    ar = []
    for i in data:
        ar.append({
            "id":i.id,
            "Name":i.Name,
        })

    return JsonResponse({"status":"ok","data":ar})

def viewprou(request):
    id=request.POST['cid']
    data = Product.objects.filter(CATEGOREY_id=id)
    ar = []
    for i in data:
        ar.append({
            "id":i.id,
            "pname":i.Pname,
            "pdate":i.Purchase_date,
            "mdate":i.Man_date,
            "price":i.Price,
            "cname":i.CATEGOREY.Name,
            "sname":i.SHOP.Sname,
            "stock":i.Stock,
            "pic":i.Image,
        })

    return JsonResponse({'status':'ok',"data":ar})

def addcart(request):
    id = request.POST['lid']
    uid = User.objects.get(LOGIN=id)
    pid = request.POST['pid']
    quantity = request.POST['quantity']

    obj = cart()
    obj.Quantity = quantity
    obj.USER = uid
    obj.PRODUCT_id = pid
    obj.save()
    return JsonResponse({'status':'ok'})

def viewcart(request):
    id = request.POST['lid']
    data = cart.objects.filter(USER__LOGIN=id)
    ar = []
    total_amount = 0
    for i in data:
        product = i.PRODUCT
        Price = product.Price
        total_pro = int(Price) * int(i.Quantity)
        total_amount += total_pro
        ar.append({
            "id":i.id,
             "pname":i.PRODUCT.Pname,
            "quantity":i.Quantity,
            "price":i.PRODUCT.Price,
            "pid":i.PRODUCT.id,
            "total_pro":total_pro,
        })
        print(ar)
    return JsonResponse({'status': 'ok', 'data': ar,"amount":total_amount})

def delete_cart(request):
    id = request.POST['cid']
    cart.objects.get(id=id).delete()
    return JsonResponse({'status':'ok'})

import datetime
from django.http import JsonResponse

def placeorder(request):
    # id = request.POST['lid']
    # uid = User.objects.get(LOGIN=id)
    #
    # data = cart.objects.filter(USER__LOGIN=id)
    #
    # ar = set()
    # for i in data:
    #     ar.add(i.PRODUCT.SHOP.id)
    #
    # for i in ar:
    #     order = Order()
    #     order.USER = uid
    #     order.SHOP_id = i
    #     order.date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    #     order.Status = 'pending'
    #     order.Amount = 0
    #     order.save()
    #
    #     total_amount = 0
    #
    #
    #     data = data.filter(PRODUCT__SHOP_id=i)
    #     for i in data:
    #         product = i.PRODUCT
    #         quantity = i.Quantity
    #         price = product.Price
    #
    #         total_pro = int(price) * int(quantity)
    #         total_amount += total_pro
    #
    #         order_sub = Order_sub()
    #         order_sub.Quantity = quantity
    #         order_sub.PRODUCT = product
    #         order_sub.ORDER = order
    #         order_sub.save()
    #
    #
    #     order.Amount = total_amount
    #     order.save()
    #
    #
    #
    # data.delete()

    return JsonResponse({'status': 'ok'})

def offline_payment(request):
    id = request.POST['lid']
    amount = request.POST['amount']
    uid = User.objects.get(LOGIN=id)

    data = cart.objects.filter(USER__LOGIN=id)
    shops = set(item.PRODUCT.SHOP.id for item in data)

    for shop_id in shops:
        shop_items = data.filter(PRODUCT__SHOP_id=shop_id)

        order = Order()
        order.USER = uid
        order.SHOP_id = shop_id
        order.date = datetime.datetime.now().strftime("%Y-%m-%d")
        order.Status = "request"
        order.payment_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        order.payment_status = 'paid'
        order.payment_method = 'offline'
        order.save()

        total_amount = 0
        product_ids = set()

        for item in shop_items:
            product = item.PRODUCT
            quantity = item.Quantity
            price = product.Price
            total_price = int(price) * int(quantity)

            total_amount += total_price

            if product.id not in product_ids:
                order_sub = Order_sub()
                order_sub.Quantity = quantity
                order_sub.PRODUCT = product
                order_sub.ORDER = order
                order_sub.save()
                product_ids.add(product.id)

        order.Amount = total_amount
        order.save()

    data.delete()

    return JsonResponse({'status': 'ok'})

def vieworderstatus(request):
    id = request.POST['lid']
    data = Order.objects.filter(USER__LOGIN=id)
    ar = []
    for i in  data:
        ar.append({
            "oid":i.id,
            "date":i.date,
            "amount":i.Amount,
            "status":i.Status,
        })

    return JsonResponse({'status':'ok','data':ar})

def vieworderpro(request):
    id = request.POST['oid']
    data = Order_sub.objects.filter(ORDER=id)
    ar = []
    for i in data:
        ar.append({
            "oid":i.id,
            "pname":i.PRODUCT.Pname,
            "quantity":i.Quantity,
            "amount":i.ORDER.Amount,
            "price":i.PRODUCT.Price,
            "sid":i.PRODUCT.SHOP_id
        })
    return JsonResponse({"status":"ok","data":ar})

def sndreview(request):
    id=request.POST['lid']
    print(id)
    sid=request.POST['sid']
    uid = User.objects.get(LOGIN=id)
    date = request.POST['date']
    review = request.POST['review']
    rating = request.POST['rating']

    if Review.objects.filter(date=date).exists() or Review.objects.filter(Review=review).exists() or Review.objects.filter(Ratings=rating).exists():
        return JsonResponse({"status": "no"})


    obj = Review()
    obj.date = date
    obj.Review = review
    obj.Ratings = rating
    obj.USER = uid
    obj.SHOP_id = sid
    print(sid)
    obj.save()
    return JsonResponse({'status':'ok'})


def SndComplaints(request):
    id=request.POST['lid']
    uid = User.objects.get(LOGIN=id)
    date = request.POST['date']
    complaints = request.POST['complaints']

    if Complaints.objects.filter(date=date).exists() or Complaints.objects.filter(complaints=complaints).exists():
        return JsonResponse({"status": "no"})



    obj = Complaints()
    obj.date = date
    obj.complaints = complaints
    obj.USER = uid
    obj.save()

    return JsonResponse({'status':'ok'})

def viewReplay(request):
    id = request.POST['lid']
    data = Complaints.objects.filter(USER__LOGIN=id)
    ar = []
    for i in data:
        ar.append({
            "id":i.id,
            "replay":i.replay,
            "rdate":i.replay_date,
        })

    return JsonResponse({'status':'ok','data':ar})

def sndfdback(request):
    id = request.POST['lid']
    uid = User.objects.get(LOGIN=id)
    date = request.POST['date']
    fdback = request.POST['fdback']

    if feedback.objects.filter(date=date).exists() or feedback.objects.filter(feedback=fdback).exists():
        return JsonResponse({"status": "no"})


    obj = feedback()
    obj.date = date
    obj.feedback = fdback
    obj.USER = uid
    obj.save()
    return JsonResponse({'status':'ok'})

def Changepswu(request):
    lid = request.POST['lid']
    cpsw = request.POST['cpsw']
    npsw = request.POST['npsw']
    copsw = request.POST['copsw']
    usertype = 'user'

    psw = login.objects.filter(password=cpsw, id=lid)
    if psw.exists():
        if npsw == copsw:
            login.objects.filter(id=lid).update(password=npsw)
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'missmated'})
    return JsonResponse({'status': 'failed'})

def forgotpasswdu(request):
    email = request.POST['email']
    d = login.objects.filter(username=email)
    if d.exists():
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("abhinavmohan778@gmail.com", "higo xdna uwjq klyz")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "abhinavmohan778@gmail.com"
        msg['To'] = d[0].username
        msg['Subject'] = "Forgeted Password"
        body = "Your Password is:- - " + str(d[0].password)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'failed'})

def online_payment(request):
    id = request.POST['lid']
    amount = request.POST['amount']
    uid = User.objects.get(LOGIN=id)

    data = cart.objects.filter(USER__LOGIN=id)
    shops = set(item.PRODUCT.SHOP.id for item in data)

    for shop_id in shops:
        shop_items = data.filter(PRODUCT__SHOP_id=shop_id)

        order = Order()
        order.USER = uid
        order.SHOP_id = shop_id
        order.date = datetime.datetime.now().strftime("%Y-%m-%d")
        order.Status = "request"
        order.payment_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        order.payment_status = 'paid'
        order.payment_method = 'online'
        order.save()

        total_amount = 0
        product_ids = set()

        for item in shop_items:
            product = item.PRODUCT
            quantity = item.Quantity
            price = product.Price
            total_price = int(price) * int(quantity)

            total_amount += total_price

            if product.id not in product_ids:
                order_sub = Order_sub()
                order_sub.Quantity = quantity
                order_sub.PRODUCT = product
                order_sub.ORDER = order
                order_sub.save()
                product_ids.add(product.id)

        order.Amount = total_amount
        order.save()

    data.delete()

    return JsonResponse({'status': 'ok'})
