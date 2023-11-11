'''
Author: codepanda codepanda@qq.com
Date: 2023-11-10 10:14:05
LastEditors: codepanda codepanda@qq.com
LastEditTime: 2023-11-10 17:15:03
FilePath: /seismic_web/seismic_backend/seismic_events/views.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from django.shortcuts import render

from geopy.distance import geodesic

from seismic_stations.models import SeismicStation

def calculate_distance(request):
    """获取表单添加的事件经纬度信息， 计算其与所有站点的距离"""
    if request.method == 'POST':
        event_latitude = request.POST.get('event_latitude')
        event_longitude = request.POST.get('event_longitude')
        event_depth = request.POST.get('event_depth')
        
        station_list = SeismicStation.objects.all()
        station_distance_list = []
        for station in station_list:
            distance = round(geodesic((event_latitude, event_longitude), (station.latitude, station.longitude)).km, 2)
            
            station_distance_list.append((station, distance))
        
        station_distance_list.sort(key=lambda x: x[1])
        
        return render(request, 'seismic_events/cal_event_station_distance.html', {
            "station_distance_list": station_distance_list
        })
    
    return render(request, 'seismic_events/cal_event_station_distance.html')
        


    
    
    