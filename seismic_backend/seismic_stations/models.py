'''
Author: codepanda codepanda@qq.com
Date: 2023-11-10 10:15:59
LastEditors: codepanda codepanda@qq.com
LastEditTime: 2023-11-10 10:19:55
FilePath: /seismic_web/seismic_backend/seismic_stations/models.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from django.db import models

class SeismicNetwork(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.code

class SeismicStation(models.Model):
    network = models.ForeignKey(SeismicNetwork, on_delete=models.CASCADE, related_name="stations")
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
