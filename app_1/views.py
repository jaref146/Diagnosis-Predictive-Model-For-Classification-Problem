from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import sale_book, contact_info_tabel, wish_list_table
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    get_sale_book = sale_book.objects.all()
    get_user_all = sale_book.objects.all().count()
    get_user_Arts_and_Music = sale_book.objects.filter(Books_category= 'Arts & Music').count()
    get_user_Biographies = sale_book.objects.filter(Books_category= 'Biographies').count()
    get_user_Business = sale_book.objects.filter(Books_category= 'Business').count()
    get_user_Comics = sale_book.objects.filter(Books_category= 'Comics').count()
    get_user_Computers_and_Tech = sale_book.objects.filter(Books_category= 'Computers & Tech').count()
    get_user_Cooking = sale_book.objects.filter(Books_category= 'Cooking').count()
    get_user_Edu_and_Reference = sale_book.objects.filter(Books_category= 'Edu & Reference').count()
    get_user_Entertainment = sale_book.objects.filter(Books_category= 'Entertainment').count()
    get_user_Special_Editions = sale_book.objects.filter(Books_category= 'Special Editions').count()
    get_user_Health_and_Fitness = sale_book.objects.filter(Books_category= 'Health & Fitness').count()
    get_user_History = sale_book.objects.filter(Books_category= 'History').count()
    get_user_Horror = sale_book.objects.filter(Books_category= 'Horror').count()
    get_user_Medical = sale_book.objects.filter(Books_category= 'Medical').count()
    get_user_Religion = sale_book.objects.filter(Books_category= 'Religion').count()
    get_user_Romance = sale_book.objects.filter(Books_category= 'Romance').count()
    get_user_Other = sale_book.objects.filter(Books_category= 'Other').count()

    contex = {
        'get_sale_book':get_sale_book,
        'get_user_all':get_user_all,
        'get_user_Arts_and_Music':get_user_Arts_and_Music,
        'get_user_Biographies':get_user_Biographies,
        'get_user_Business':get_user_Business,
        'get_user_Comics':get_user_Comics,
        'get_user_Computers_and_Tech':get_user_Computers_and_Tech,
        'get_user_Cooking':get_user_Cooking,
        'get_user_Edu_and_Reference':get_user_Edu_and_Reference,
        'get_user_Entertainment':get_user_Entertainment,
        'get_user_Special_Editions':get_user_Special_Editions,
        'get_user_Health_and_Fitness':get_user_Health_and_Fitness,
        'get_user_History':get_user_History,
        'get_user_Horror':get_user_Horror,
        'get_user_Medical':get_user_Medical,
        'get_user_Religion':get_user_Religion,
        'get_user_Romance':get_user_Romance,
        'get_user_Other':get_user_Other


    }
    return render(request, 'index.html', contex)


def spacific_category(request, pk_id):
    get_sale_book = sale_book.objects.filter(Books_category=pk_id)
    get_user_all = sale_book.objects.all().count()
    get_user_Arts_and_Music = sale_book.objects.filter(Books_category='Arts & Music').count()
    get_user_Biographies = sale_book.objects.filter(Books_category='Biographies').count()
    get_user_Business = sale_book.objects.filter(Books_category='Business').count()
    get_user_Comics = sale_book.objects.filter(Books_category='Comics').count()
    get_user_Computers_and_Tech = sale_book.objects.filter(Books_category='Computers & Tech').count()
    get_user_Cooking = sale_book.objects.filter(Books_category='Cooking').count()
    get_user_Edu_and_Reference = sale_book.objects.filter(Books_category='Edu & Reference').count()
    get_user_Entertainment = sale_book.objects.filter(Books_category='Entertainment').count()
    get_user_Special_Editions = sale_book.objects.filter(Books_category='Special Editions').count()
    get_user_Health_and_Fitness = sale_book.objects.filter(Books_category='Health & Fitness').count()
    get_user_History = sale_book.objects.filter(Books_category='History').count()
    get_user_Horror = sale_book.objects.filter(Books_category='Horror').count()
    get_user_Medical = sale_book.objects.filter(Books_category='Medical').count()
    get_user_Religion = sale_book.objects.filter(Books_category='Religion').count()
    get_user_Romance = sale_book.objects.filter(Books_category='Romance').count()
    get_user_Other = sale_book.objects.filter(Books_category='Other').count()
    contex = {
        'get_sale_book': get_sale_book,
        'cetagory_type': pk_id,
        'get_user_all': get_user_all,
        'get_user_Arts_and_Music': get_user_Arts_and_Music,
        'get_user_Biographies': get_user_Biographies,
        'get_user_Business': get_user_Business,
        'get_user_Comics': get_user_Comics,
        'get_user_Computers_and_Tech': get_user_Computers_and_Tech,
        'get_user_Cooking': get_user_Cooking,
        'get_user_Edu_and_Reference': get_user_Edu_and_Reference,
        'get_user_Entertainment': get_user_Entertainment,
        'get_user_Special_Editions': get_user_Special_Editions,
        'get_user_Health_and_Fitness': get_user_Health_and_Fitness,
        'get_user_History': get_user_History,
        'get_user_Horror': get_user_Horror,
        'get_user_Medical': get_user_Medical,
        'get_user_Religion': get_user_Religion,
        'get_user_Romance': get_user_Romance,
        'get_user_Other': get_user_Other
    }
    return render(request, 'index.html', contex)



def post_details(request,pk_id):
    if request.user.is_authenticated:
        info_get = sale_book.objects.get(id=pk_id)
        contex = {
            'info_get':info_get
        }
        return render(request, 'post_details_page.html', contex)
    else:
        return redirect('Login_or_Register_page')


def search_things_url(request):
    if request.method=='POST':
        search_things = request.POST.get('search_things')

        if search_things:
            get_sale_book = sale_book.objects.filter(store_post_book_name__contains = search_things)
            contex = {
                'cetagory_type': search_things,
                'get_sale_book': get_sale_book
            }
            return render(request, 'index.html', contex)
        return redirect('index')
    return redirect('index')


def Login_or_Register_page(request):
    return render(request, 'login_or_register.html')



def go_for_Register(request):
    if request.method == "POST":
        Register_First_Name=request.POST.get('Register_First_Name')
        Register_Last_Name=request.POST.get('Register_Last_Name')
        Register_Enter_Email=request.POST.get('Register_Enter_Email')
        Register_Password=request.POST.get('Register_Password')
        Register_Confirm_Password=request.POST.get('Register_Confirm_Password')
        if Register_Confirm_Password == Register_Password:
            myusr_vari = User.objects.create_user(Register_Enter_Email, Register_Enter_Email, Register_Password)
            myusr_vari.first_name=Register_First_Name
            myusr_vari.last_name=Register_Last_Name
            myusr_vari.save()
        else:
            massage = "Your Password is not match"
            contex = {
                'massage':massage
            }
            return render(request, 'login_or_register.html', contex)
        massage_4 = "Account is created successfully"
        contex = {
            'massage_4': massage_4
        }
    return render(request, 'login_or_register.html', contex)


def Edit_profil(request):
    if request.user.is_authenticated:
        Edit_profilRegister_First_Name = request.POST.get('Edit_profilRegister_First_Name')
        Edit_profilRegister_Last_Name = request.POST.get('Edit_profilRegister_Last_Name')
        Edit_profilRegister_Enter_Email = request.POST.get('Edit_profilRegister_Enter_Email')
        Edit_profil_old_Register_Password = request.POST.get('Edit_profil_old_Register_Password')
        Edit_profil_New_Register_Password = request.POST.get('Edit_profil_New_Register_Password')
        Edit_profil_Confirm_New_Register_Password = request.POST.get('Edit_profil_Confirm_New_Register_Password')

        if Edit_profil_old_Register_Password:
            user_vari = authenticate(username=request.user.email, password=Edit_profil_old_Register_Password)

            if user_vari is not None and Edit_profil_New_Register_Password == Edit_profil_Confirm_New_Register_Password:

                get_info_of_user = User.objects.get(username = request.user.username)
                get_info_of_user.first_name = Edit_profilRegister_First_Name
                get_info_of_user.last_name = Edit_profilRegister_Last_Name
                get_info_of_user.username = Edit_profilRegister_Enter_Email
                get_info_of_user.email = Edit_profilRegister_Enter_Email
                get_info_of_user.password = make_password(Edit_profil_Confirm_New_Register_Password)
                get_info_of_user.save()

                user_vari = authenticate(username=Edit_profilRegister_Enter_Email, password=Edit_profil_Confirm_New_Register_Password)
                if user_vari is not None:
                    login(request, user_vari)

                masage_3 = 'your Information updated'

                get_info_of_user = User.objects.get(username=request.user.username)
                contex = {
                    'get_info_of_user': get_info_of_user,
                    'masage_3': masage_3
                }
                return render(request, 'profile_page.html', contex)
            else:
                masage_2 = 'your old password dose not match'

                get_info_of_user = User.objects.get(username=request.user.username)
                contex = {
                    'get_info_of_user': get_info_of_user,
                    'masage_2': masage_2
                }

                return render(request, 'profile_page.html', contex)
        else:

            get_info_of_user = User.objects.get(username=request.user.username)


            get_info_of_user.first_name = Edit_profilRegister_First_Name
            get_info_of_user.last_name = Edit_profilRegister_Last_Name
            get_info_of_user.username = Edit_profilRegister_Enter_Email
            get_info_of_user.email = Edit_profilRegister_Enter_Email

            get_info_of_user.save()


            masage_3 = 'your Information updated'

            get_info_of_user = User.objects.get(username=request.user.username)
            contex = {
                'get_info_of_user': get_info_of_user,
                'masage_3': masage_3
            }
            return render(request, 'profile_page.html', contex)
    else:
        return render(request, 'login_or_register.html')



def go_for_login(request):
    if request.method=="POST":
        Login_Email_Address = request.POST.get('Login_Email_Address')
        Login_Password = request.POST.get('Login_Password')

        user_vari = authenticate(username=Login_Email_Address, password=Login_Password)
        if user_vari is not None:
            login(request, user_vari)

            return redirect('index')
        else:
            contex = {
                'mas':'Your credentials are wrong'
            }
            return render(request, 'login_or_register.html', contex)

    return render(request, 'login_or_register.html')


def My_account_page(request):
    if request.user.is_authenticated:
        return render(request, 'My_account_page_html.html')
    else:
        return render(request, 'login_or_register.html')


def Profile_page(request):
    if request.user.is_authenticated:
        get_info_of_user = User.objects.get(username = request.user.username)
        contex = {
            'get_info_of_user':get_info_of_user
        }
        return render(request, 'profile_page.html', contex)

    else:
        return render(request, 'login_or_register.html')




def POST_FOR_SALE(request):
    if request.user.is_authenticated:
        get_info_of_user = User.objects.get(username=request.user.username)
        get_info_of_user_post = sale_book.objects.filter(store_user=get_info_of_user)
        contex = {
            'get_info_of_user': get_info_of_user,
            'get_info_of_user_post':get_info_of_user_post
        }
        return render(request, 'get_post_from.html', contex)

    else:
        return render(request, 'login_or_register.html')


def POST_FOR_SALE22(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            post_book_name = request.POST.get('post_book_name')
            post_book_user_email = request.POST.get('post_book_user_email')
            post_book_user_number = request.POST.get('post_book_user_number')
            post_book_subject = request.POST.get('post_book_subject')
            post_book_description = request.POST.get('post_book_description')
            post_book_price = request.POST.get('post_book_price')
            post_books_category = request.POST.get('post_books_category')
            post_book_image = request.FILES.get('post_book_image')

            print('post_books_categorypost_books_categorypost_books_category')
            print('post_books_category')
            print(post_books_category)

            fs = FileSystemStorage()
            filename = fs.save(post_book_image.name, post_book_image)
            uploaded_file_url = fs.url(filename)

            p_get_Login_Email_Address = User.objects.get(username = request.user.username)

            save_sale_book = sale_book(store_user = p_get_Login_Email_Address, Books_category= post_books_category, store_post_book_name = post_book_name, store_post_book_price = post_book_price,store_post_book_user_email = post_book_user_email, store_post_book_user_number = post_book_user_number,  store_post_book_subject = post_book_subject, store_post_book_description = post_book_description, store_post_book_image = uploaded_file_url)
            save_sale_book.save()
            return redirect('POST_FOR_SALE')


def Remove_Post(request, pk_id):
    get_data = sale_book.objects.get(id = pk_id)
    get_data.delete()
    return redirect('POST_FOR_SALE')


def Log_out_page(request):
    # this is for logout from user id
    logout(request)
    return redirect('index')

def about(request):
    return render(request, 'about_page.html')


def contact_us(request):
    return render(request, 'contact_us_page.html')
def conteact_persion_info(request):
    if request.method=='POST':
        conteact_persion_name = request.POST.get('conteact_persion_name')
        conteact_persion_email = request.POST.get('conteact_persion_email')
        conteact_persion_subjects = request.POST.get('conteact_persion_subjects')
        conteact_persion_massage = request.POST.get('conteact_persion_massage')

        get_contact_info_tabel = contact_info_tabel(contact_persions_name = conteact_persion_name, contact_persions_email = conteact_persion_email, contact_persions_subjects =conteact_persion_subjects, contact_persions_massages = conteact_persion_massage)
        get_contact_info_tabel.save()

        contex= {
            'massage':'Thanks for your massage'
        }
        return render(request, 'contact_us_page.html', contex)
    return render(request, 'contact_us_page.html')



@csrf_exempt
def save_wishlist(request):
    product_id = request.POST.get('product_id')
    get_product = sale_book.objects.get(id=product_id)
    usr = request.user
    get_wish_list_table = wish_list_table(Wish_persions = usr, Wish_product=get_product)
    get_wish_list_table.save()

    return HttpResponse(True)


def Wish_List_Show(request):
    usr = request.user
    if request.user.is_authenticated:
        get_data = wish_list_table.objects.filter(Wish_persions=usr)
        contex = {
            'get_data': get_data
        }
        return render(request, 'wish_list_page.html', contex)

    else:
        return render(request, 'login_or_register.html')


def delete_wish_list(request, pk_id):
    if request.user.is_authenticated:
        get_data = wish_list_table.objects.get(id = pk_id)
        get_data.delete()
        usr = request.user
        get_data = wish_list_table.objects.filter(Wish_persions=usr)
        contex={
            'get_data':get_data
        }
        return render(request, 'wish_list_page.html', contex)