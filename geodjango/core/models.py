#coding: utf-8
from django.contrib.gis.db import models
from reversegeo.openstreetmap import OpenStreetMap

class Land(models.Model):
    area = models.PolygonField()
    objects = models.GeoManager()


class Place(models.Model):
    name = models.CharField(max_length=128)
    coord = models.PointField()
    address = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("place-detail", [self.id,])

    def address_from_coord(self, format_string=''):
        ''' use openstreetmap reverse geocoder 
        '''
        g = OpenStreetMap()
        if format_string == '':
            ret = g.reverse(self.coord, default=str(self.coord))
        else:
            ret = g.reverse(self.coord, format_string=format_string)
        return ret

    def compute_orientation(self, lat, lon):
        ''' orientation around point lat, lon to self '''
        return atan2(self.coord.y - lat, self.coord.x - lon) * 57.2957795 # convert radians to deg

    def compute_distance(self, lat, lon):
        ''' compute distance to lat,lon '''
        point = (lat, lon)
        coord = (self.coord.y, self.coord.x)
        return distance.distance(coord, point).miles
        
    def __unicode__(self):
        return self.name

