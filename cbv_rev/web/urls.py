from django.urls import path

from cbv_rev.web.views import IndexView, IndexViewWithTemplate

urlpatterns = (
    path('', IndexViewWithTemplate.as_view()),
    # path('2/', Index2View.get_view()),
)
