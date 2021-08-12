from django.urls import path
from .views import CourseView,CourseViewWithId,ClassCourseView,CurdMixinView,GenericBasedView
urlpatterns=[
    path('',CourseView,name='courseview'),
    path('courseViewWithId/<int:pk>/',CourseViewWithId,name='cwithid'),
    path('classbasedviewwithid/<int:pk>/',ClassCourseView.as_view(),name='classbased'),
    path('mixin/<int:pk>/',CurdMixinView.as_view(),name='mixin'),
    path('genericbasedview/<int:pk>/',GenericBasedView.as_view(),name='genericbasedview')
]