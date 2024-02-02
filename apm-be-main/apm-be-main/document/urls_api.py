from django.urls import path

from . import views_api
from .views_api import ProjectDocumentRetrieveUpdate, ProjectDocumentListSearch, export_documents_to_excel

urlpatterns = [
    path('', views_api.ProjectDocumentListCreate.as_view(), name='document-list-create'),
    path('edit/<int:pk>/', ProjectDocumentRetrieveUpdate.as_view(), name='document-retrieve-update'),
    path('search/', ProjectDocumentListSearch.as_view(), name='document-list-search'),
    path('export-documents-to-excel/', export_documents_to_excel, name='export-documents-to-excel'),

]