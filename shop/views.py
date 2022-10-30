from uuid import UUID
from django.shortcuts import render
from .models import Contact, Product, Order, Tracker

# Home page of the site
def index(request):
    categories = Product.objects.values('Catagory','Prod_Id')
    categoriesProduct = { item['Catagory'] for item in categories}
    allProducts = []
    for cat in categoriesProduct:
        prod = Product.objects.filter(Catagory = cat)
        allProducts.append([cat,prod])
    params = { 'products':allProducts }
    return render(request,'index.html',params)

# function to check whether given word is present in item or not
def matchQuery(query,item):
    name = str(query).lower() in str(item.Product_Name).lower()
    cat = str(query).lower() in str(item.Catagory).lower()
    scat = str(query).lower() in str(item.Sub_Catagory).lower()
    disc = str(query).lower() in str(item.Discription).lower()
    print(name)
    return name or cat or scat or disc

# searching of item(s)
def search(request):
    keyword = request.GET.get('keyword','')
    categories = Product.objects.values('Catagory','Prod_Id')
    categoriesProduct = { item['Catagory'] for item in categories}
    print(categoriesProduct)
    allProducts = []
    for cat in categoriesProduct:
        tempProd = Product.objects.filter(Catagory = cat)
        prod = [item for item in tempProd if matchQuery(keyword,item)]
        print(prod)
        if(len(prod)!=0):
            allProducts.append([cat,prod])
    params = { 'products':allProducts }
    return render(request,'index.html',params)

#about page of site
def about(request):
    return render(request,'about.html')

#tracker to track orders
def tracker(request):
    if(request.method=='POST'):
        print('Post Request recieved')
        id = request.POST.get('id','null')
        if(is_valid_uuid(id)):
            track = Tracker.objects.filter(Tracking_Id=id)
            order = (Order.objects.filter(Order_ID=id))[0]
            items = order.Json_Data
            if(len(track)==0):
                return render(request,'Tracker.html',{'err': True})
            return render(request,'Tracker.html',{'stat':track[0],'items':items})
        else:
            return render(request,'Tracker.html',{'err': True})      
    return render(request,'Tracker.html')


def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        discription = request.POST.get('discription')
        query = Contact(Name=name,Email=email,Discription=discription)
        query.save()
        flag = True
        return render(request,'contact.html',{'flag':flag})
    return render(request,'contact.html')

# product view
def product_view(request,id):
    product = Product.objects.filter(Prod_Id = id)
    param = { 'product':product[0] }
    return render(request,'product.html',param)

# handles order of single product
def checkoutSingleProduct(request,id):
    product = Product.objects.filter(Prod_Id = id)
    return render(request,'checkoutSingle.html',{'item':product[0]})

# handles order of multiple product
def checkoutMultiProd(request):
    print(request.POST.get('data'))
    return render(request,'checkoutMulti.html')

# function triggers when order is about to confirm
def conformation(request):
    id=''
    if request.method=='POST':
        email = request.POST.get('email','')
        state = request.POST.get('state','')
        city = request.POST.get('city','')
        address = request.POST.get('address','')
        country = request.POST.get('country','')
        lname = request.POST.get('lname','')
        fname = request.POST.get('fname','')
        amount = request.POST.get('amount','')
        jsondata = request.POST.get('jsonobject','')
        zip = int(request.POST.get('zip',''))
        order = Order(Amount=amount,Name=fname+" "+lname, Email=email, Country=country, Address=address,City=city, State=state,Zip=zip, Json_Data=jsondata)
        order.save()
        id=order.Order_ID
        track = Tracker(Tracking_Id = order)
        track.save()
    return render(request,'conformation.html',{'id':id})

# function to check for valid uuid
def is_valid_uuid(uuid_to_test, version=4):
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test