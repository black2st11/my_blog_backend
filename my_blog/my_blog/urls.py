"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('me', include('me.urls')),
    path('achievement', include('achievement.urls')),
    path('dungeon', include('dungeon.urls')),
    path('career', include('career.urls')),
    path('post', include('post.urls')),
    path('question', include('qna.urls')),
    path('main', include('main.urls'))
]

# urlpatterns +=[
#         path('__debug__/', include('debug_toolbar.urls')),
#     ]
