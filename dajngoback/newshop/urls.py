from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('newshonContact/',views.NewContactView.as_view()),
    path('prod/',views.ProductView.as_view()),
    path('singelprodview/<int:pk>',views.SingleProductView.as_view()),
    path('categorywiseview/',views.CategoryWiseView.as_view()),
    path('order/',views.NewOrder.as_view()),
    path('OrderUpdate/',views.OrderUpdateView.as_view()),
    path('cartData/<str:email>',views.CartUpdateView.as_view()),
    path('cartCreate/',views.CartCreateView.as_view()),
    path('cartGet/<str:email>',views.GetCartView.as_view()),
    path('excel/',views.export_data_to_excel),
    path('excelimport/',views.import_data_to_db),
    path('contactpdf/',views.contact_pdf.as_view()),
    path('browserexcel/',views.export_to_excel_on_download),
    path('downloadexcelfolder/',views.import_exce_in_folder),
    path('setcoockies/',views.SetCookieView.as_view()),
    path('getcoockies/',views.GetCookieView.as_view()),
    path('deletecoockies/',views.DeleteCookieView.as_view()),
    path('setsession/',views.SetSessionView.as_view()),
    path('getsession/',views.GetSessionView.as_view()),
    path('delsession/',views.DeleteSessionView.as_view()),
    path('settokensession/',views.SetTokensession.as_view()),
    path('gettokensession/',views.getTokensession.as_view()),
    path('deltokensession/',views.deleteTokenSession.as_view()),
]
    