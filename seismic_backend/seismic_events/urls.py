'''
Author: codepanda codepanda@qq.com
Date: 2023-11-10 16:55:46
LastEditors: codepanda codepanda@qq.com
LastEditTime: 2023-11-10 16:57:36
FilePath: /seismic_web/seismic_backend/seismic_events/urls.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from django.contrib import admin
from django.urls import path

from .views import calculate_distance

urlpatterns = [
    path('seismic_events/calculate_distance', calculate_distance),
]
