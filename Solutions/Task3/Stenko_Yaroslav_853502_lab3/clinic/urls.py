from django.urls import path

from clinic.views import DoctorListView, doctor_detail_view, schedule_create_view, schedule_edit_view,\
    schedule_delete_view, comment_create_view, comment_edit_view, comment_delete_view


urlpatterns =[
    path('', DoctorListView.as_view(), name='doctor'),
    path('doctors/<int:doctor_id>/', doctor_detail_view, name='doctor_detail'),
    path('add/', schedule_create_view, name='schedule_create'),
    path('<int:schedule_id>/edit/', schedule_edit_view, name='schedule_edit'),
    path('<int:schedule_id>/delete/', schedule_delete_view, name='schedule_delete'),
    path('<int:doctor_id>/comment/add', comment_create_view, name='comment_add'),
    path('<int:comment_id>/edit', comment_edit_view, name='comment_edit'),
    path('<int:comment_id>/delete', comment_delete_view, name='comment_delete')
]
