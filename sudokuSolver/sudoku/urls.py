from django.urls import path
from . import views

urlpatterns = [
    path('bytype/<int:pk>', views.solveByType, name="sudoku_solve_by_type"),
    path('bytype/', views.solveByType),
    path('bypic/', views.solveByPicCBV.as_view()),
    path('bypic/<int:pk>', views.solveByPic, name="img_uploaded"),
    path('posts/', views.PostListView.as_view()),
]