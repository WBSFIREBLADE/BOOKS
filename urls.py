from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", v.home, name='Home' ),
    path("aboutus", v.aboutus, name= "about us"),
    path("help", v.h, name='h'),
    path ("signup/", v.sign_up, name='signup' ),
    path("login/", v.log_in, name='login'),
    path('profile/', v.profile, name='profile'),
    path('logout/', v.log_out, name='logout'),
    path('L',v.L,name='L'),
    path('S',v.S,name='S'),
    path('F',v.F,name='F'),
    path('K',v.K,name='K'),
    path('Search_Book', v.Seach_Book, name='Book'),
    path('pcf', v.pcf, name='pcf'),
    path('my_view/<int:id>/', v.my_view, name='KB'),
    path('my_viewL/<int:id>/', v.my_viewL, name='LB'),
    path('my_viewS/<int:id>/', v.my_viewS, name='SB'),
    path('my_viewT/<int:id>/', v.my_viewT, name='TB'),
    path('add-to-cart/<int:id>/', v.add_to_cart, name='add_to_cart'),
    path('add-to-cartL/<int:id>/', v.add_to_cartL, name='add_to_cartL'),
    path('add-to-cartS/<int:id>/', v.add_to_cartS, name='add_to_cartS'),
    path('add-to-cartT/<int:id>/', v.add_to_cartT, name='add_to_cartT'),
    path('view-cart/', v.view_cart, name='view_cart'),
    path('add_quantity/<int:id>/', v.add_quantity, name='add_quantity'),
    path('delete_quantity/<int:id>/', v.delete_quantity, name='delete_quantity'),
    path('add_quantityL/<int:id>/', v.add_quantityL, name='add_quantityL'),
    path('delete_quantityL/<int:id>/', v.delete_quantityL, name='delete_quantityL'),
    path('add_quantityS/<int:id>/', v.add_quantityS, name='add_quantityS'),
    path('delete_quantityS/<int:id>/', v.delete_quantityS, name='delete_quantityS'),
    path('add_quantityT/<int:id>/', v.add_quantityT, name='add_quantityT'),
    path('delete_quantityT/<int:id>/', v.delete_quantityT, name='delete_quantityT'),
    path('delete/<int:id>/', v.delete, name='delete_K'),
    path('deleteL/<int:id>/', v.deleteL, name='delete_L'),
    path('deleteS/<int:id>/', v.deleteS, name='delete_S'),
    path('deleteT/<int:id>/', v.deleteT, name='delete_T'),
    path('adress', v.address, name='address'),
    path('delete_address/<int:id>', v.delete_address, name='deleteaddress'),
    path('Checkout', v.Chekcout, name='Checkout'),
    path('Payment/',v.Payment,name='payment'),
    path('payment_success/<int:selected_address_id>/',v.payment_success,name='paymentsuccess'),

    path('payment_failed/',v.payment_failed,name='paymentfailed'),
    path('order/',v.order,name='order'),
    path('Buynow/<int:id>/',v.Buynow,name='buynow'),
    path('Buynowl/<int:id>/',v.Buynowl,name='buynowl'),
    path('BuynowS/<int:id>/',v.BuynowS,name='buynowS'),
    path('BuynowT/<int:id>/',v.BuynowT,name='buynowT'),
    path('Buy_Now_Payment/<int:id>/',v.Buy_Now_Payment,name='buynowpayment'),
    path('buynow_payment_success/<int:selected_address_id>/<int:id>/',v.buynow_payment_success,name='buynowpaymentsuccess'),
    path('Buy_Now_Paymentl/<int:id>/',v.Buy_Now_Paymentl,name='buynowpaymentl'),
    path('buynow_payment_successl/<int:selected_address_id>/<int:id>/',v.buynow_payment_successl,name='buynowpaymentsuccessl'),
    path('Buy_Now_PaymentS/<int:id>/',v.Buy_Now_PaymentS,name='buynowpayments'),
    path('buynow_payment_successS/<int:selected_address_id>/<int:id>/',v.buynow_payment_successS,name='buynowpaymentsuccesss'),
    path('Buy_Now_PaymentT/<int:id>/',v.Buy_Now_PaymentT,name='buynowpaymentt'),
    path('buynow_payment_successT/<int:selected_address_id>/<int:id>/',v.buynow_payment_successT,name='buynowpaymentsuccesst'),
   


    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)