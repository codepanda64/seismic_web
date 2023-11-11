'''
Author: codepanda codepanda@qq.com
Date: 2023-11-10 10:15:59
LastEditors: codepanda codepanda@qq.com
LastEditTime: 2023-11-10 17:06:18
FilePath: /seismic_web/seismic_backend/seismic_stations/admin.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from django.contrib import admin

from .models import SeismicNetwork, SeismicStation


admin.site.register(SeismicNetwork)
admin.site.register(SeismicStation)