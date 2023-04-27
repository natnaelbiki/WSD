from django.urls import path
from . import views
from .views import HomePageView, ManagerSearchResultsView, BranchSearchResultsView, ManagerView, BranchView

urlpatterns = [
    path("manager_search/", ManagerSearchResultsView.as_view(), name="search_manager"),
    path("branch_search/", BranchSearchResultsView.as_view(), name="search_branch"),
    path("managers/", ManagerView.as_view(), name='manager'),
    path("branchs/", BranchView.as_view(), name='branch'),
    path("", views.testing, name="home"),
]