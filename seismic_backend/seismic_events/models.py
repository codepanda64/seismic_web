'''
Author: codepanda codepanda@qq.com
Date: 2023-10-06 16:52:45
LastEditors: codepanda codepanda@qq.com
LastEditTime: 2023-11-10 16:25:18
FilePath: /seismic_website/seismic_website/seismic_events/models.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from django.db import models

    # 添加其他字段根据需要

class SeismicEvent(models.Model):
    location_name = models.CharField(max_length=100)
    origin_time = models.DateTimeField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    magnitude_Mb = models.FloatField(blank=True, null=True)
    magnitude_Ms = models.FloatField(blank=True, null=True)
    magnitude_Ml = models.FloatField(blank=True, null=True)
    event_type = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 添加其他字段根据需要

    def __str__(self):
        return f'{self.location_name} - {self.origin_time}'
    
    class Meta:
        ordering = ('-origin_time',)
        unique_together = ('origin_time', 'location_name')

class FocalMechanismSolution(models.Model):
    seismic_event = models.ForeignKey(SeismicEvent, on_delete=models.CASCADE, related_name="solutions")
    method_name = models.CharField(max_length=100)
    strike1 = models.FloatField(blank=True, null=True)
    dip1 = models.FloatField(blank=True, null=True)
    rake1 = models.FloatField(blank=True, null=True)
    strike2 = models.FloatField(blank=True, null=True)
    dip2 = models.FloatField(blank=True, null=True)
    rake2 = models.FloatField(blank=True, null=True)
    P = models.FloatField(blank=True, null=True)
    B = models.FloatField(blank=True, null=True)
    T = models.FloatField(blank=True, null=True)
    magnitude_Mw = models.FloatField(blank=True, null=True)
    manner = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 添加其他字段根据需要

    def __str__(self):
        return f'Source Parameters - ID: {self.id}'
