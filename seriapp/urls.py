from django.urls import path,include
from .views import CourseView,CourseViewWithId,ClassCourseView,CurdMixinView,GenericBasedView,ClassViewSetsView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('courseviewsets',ClassViewSetsView)
urlpatterns=[
    path('',include(router.urls)),
    # path('',CourseView,name='courseview'),
    # path('courseViewWithId/<int:pk>/',CourseViewWithId,name='cwithid'),
    # path('classbasedviewwithid/<int:pk>/',ClassCourseView.as_view(),name='classbased'),
    # path('mixin/<int:pk>/',CurdMixinView.as_view(),name='mixin'),
    path('genericbasedview/<int:pk>/',GenericBasedView.as_view(),name='genericbasedview'),

]