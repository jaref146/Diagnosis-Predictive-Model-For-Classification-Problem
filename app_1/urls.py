from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('Login_or_Register_page/', views.Login_or_Register_page, name='Login_or_Register_page'),
    path('go_for_Register/', views.go_for_Register, name='go_for_Register'),
    path('go_for_login/', views.go_for_login, name='go_for_login'),
    path('My_account_page/', views.My_account_page, name='My_account_page'),
    path('Log_out_page/', views.Log_out_page, name='Log_out_page'),
    path('Profile_page/', views.Profile_page, name='Profile_page'),
    path('Edit_profil/', views.Edit_profil, name='Edit_profil'),
    path('POST_FOR_SALE/', views.POST_FOR_SALE, name='POST_FOR_SALE'),
    path('POST_FOR_SALE22/', views.POST_FOR_SALE22, name='POST_FOR_SALE22'),
    path('post_details/<int:pk_id>', views.post_details, name='post_details'),
    path('Remove_Post/<int:pk_id>', views.Remove_Post, name='Remove_Post'),
    path('spacific_category/<str:pk_id>', views.spacific_category, name='spacific_category'),
    path('search_things_url/', views.search_things_url, name='search_things_url'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('conteact_persion_info/', views.conteact_persion_info, name='conteact_persion_info'),
    path('save_wishlist', views.save_wishlist, name="save_wishlist"),
    path('Wish_List_Show', views.Wish_List_Show, name="Wish_List_Show"),
    path('delete_wish_list/<int:pk_id>', views.delete_wish_list, name="delete_wish_list"),
]