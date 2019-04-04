from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^$', views.awwa_today, name = 'AwwaToday'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),
    url(r'^api/projects/$', views.ProjectList.as_view(), name= 'project_list'),
    url(r'^api/profiles/$', views.ProfileList.as_view(), name= 'profile_list')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    