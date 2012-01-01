"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import time
from datetime import datetime
from django.test import TestCase
from project.apps.account.mongo import *
from project.libs.constants import GENDER_CHOICES

class AccountMongoTest(TestCase):
    def _create_records(self, number=100):
        for record in xrange(number):
            Profile.managers.save({
                'user'      : 1 if record < 50 else 2,
                'birthday'  : datetime.now(),
                'gender'    : GENDER_CHOICES[0][0] if record < 50 else GENDER_CHOICES[1][0],
                'bio'       : "Bio %s" % record
            })
    
    def _read_all(self):
        # read + compare
        read_all = Profile.managers.all(None)
        
        print "%s = 0" % read_all['meta']['current_total']
        self.assertEqual( read_all['meta']['current_total'], 0 )
        
        print "%s = 0" % read_all['meta']['total_count']
        self.assertEqual( read_all['meta']['total_count'], 0 )
        
        print "%s = []" % read_all['objects']
        self.assertEqual( read_all['objects'], [] )
    
    def test_read_create(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        print "AccountMongoTest:test_read"
        
        # empty
        Profile.managers.delete()
        
        self._read_all()
        
        # create 100 records
        self._create_records()
        
        # read all
        read_all    = Profile.managers.all(None)
        
        print "%s = 100" % read_all['meta']['total_count']
        self.assertEqual( read_all['meta']['total_count'], 100 )
        
        # read filter
        filter1 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[0][0] })
        print "%s = 50" % filter1['meta']['total_count']
        self.assertEqual( filter1['meta']['total_count'], 50 )
        
        filter2 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[1][0] })
        print "%s = 50" % filter2['meta']['total_count']
        self.assertEqual( filter2['meta']['total_count'], 50 )
        
        filter3 = Profile.managers.filter(None, { 'user' : 1 })
        print "%s = 50" % filter3['meta']['total_count']
        self.assertEqual( filter3['meta']['total_count'], 50 )
        
        filter4 = Profile.managers.filter(None, { 'user' : 2 })
        print "%s = 50" % filter4['meta']['total_count']
        self.assertEqual( filter4['meta']['total_count'], 50 )
        
        # delete
        Profile.managers.delete()
        
        # read
        self._read_all()
        
    def test_update(self):
        # empty
        Profile.managers.delete()
        
        # read + compare
        self._read_all()
        
        # create 100 records
        self._create_records()
        
        # read + compare
        read_all    = Profile.managers.all(None)
        
        print "%s = 100" % read_all['meta']['total_count']
        self.assertEqual( read_all['meta']['total_count'], 100 )
        
        # read filter
        filter1 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[0][0] })
        print "%s = 50" % filter1['meta']['total_count']
        self.assertEqual( filter1['meta']['total_count'], 50 )
        
        filter2 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[1][0] })
        print "%s = 50" % filter2['meta']['total_count']
        self.assertEqual( filter2['meta']['total_count'], 50 )
        
        filter3 = Profile.managers.filter(None, { 'user' : 1 })
        print "%s = 50" % filter3['meta']['total_count']
        self.assertEqual( filter3['meta']['total_count'], 50 )
        
        filter4 = Profile.managers.filter(None, { 'user' : 2 })
        print "%s = 50" % filter4['meta']['total_count']
        self.assertEqual( filter4['meta']['total_count'], 50 )
        
        # update (once)
        print Profile.managers.update({ 'gender' : GENDER_CHOICES[0][0] }, { '$set' : { 'gender' : GENDER_CHOICES[1][0] }})
        print Profile.managers.update({ 'user' : 1 }, { '$set' : { 'user' : 2 }})
        
        # read + compare
        filter5 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[1][0] })
        print "%s = 51" % filter5['meta']['total_count']
        self.assertEqual( filter5['meta']['total_count'], 51 )
        
        filter6 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[0][0] })
        print "%s = 49" % filter6['meta']['total_count']
        self.assertEqual( filter6['meta']['total_count'], 49 )
        
        filter7 = Profile.managers.filter(None, { 'user' : 1 })
        print "%s = 49" % filter7['meta']['total_count']
        self.assertEqual( filter7['meta']['total_count'], 49 )
        
        filter8 = Profile.managers.filter(None, { 'user' : 2 })
        print "%s = 51" % filter8['meta']['total_count']
        self.assertEqual( filter8['meta']['total_count'], 51 )
        
        # update (all)
        print Profile.managers.update_all({ 'gender' : GENDER_CHOICES[0][0] }, { '$set' : { 'gender' : GENDER_CHOICES[1][0] }})
        print Profile.managers.update_all({ 'user' : 1 }, { '$set' : { 'user' : 2 }})
        
        # read + compare
        filter9 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[1][0] })
        print "%s = 100" % filter9['meta']['total_count']
        self.assertEqual( filter9['meta']['total_count'], 100 )
        
        filter10 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[0][0] })
        print "%s = 0" % filter10['meta']['total_count']
        self.assertEqual( filter10['meta']['total_count'], 0 )
        
        filter11 = Profile.managers.filter(None, { 'user' : 1 })
        print "%s = 0" % filter11['meta']['total_count']
        self.assertEqual( filter11['meta']['total_count'], 0 )
        
        filter12 = Profile.managers.filter(None, { 'user' : 2 })
        print "%s = 100" % filter12['meta']['total_count']
        self.assertEqual( filter12['meta']['total_count'], 100 )
        
        # delete
        Profile.managers.delete()
        
        # read
        self._read_all()
    
    def test_delete(self):
        pass
        # read + compare
        self._read_all()
        
        # create
        self._create_records()
        
        # read + compare
        read_all    = Profile.managers.all(None)
        
        print "%s = 100" % read_all['meta']['total_count']
        self.assertEqual( read_all['meta']['total_count'], 100 )
        
        # read filter
        filter1 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[0][0] })
        print "%s = 50" % filter1['meta']['total_count']
        self.assertEqual( filter1['meta']['total_count'], 50 )
        
        filter2 = Profile.managers.filter(None, { 'gender' : GENDER_CHOICES[1][0] })
        print "%s = 50" % filter2['meta']['total_count']
        self.assertEqual( filter2['meta']['total_count'], 50 )
        
        filter3 = Profile.managers.filter(None, { 'user' : 1 })
        print "%s = 50" % filter3['meta']['total_count']
        self.assertEqual( filter3['meta']['total_count'], 50 )
        
        filter4 = Profile.managers.filter(None, { 'user' : 2 })
        print "%s = 50" % filter4['meta']['total_count']
        self.assertEqual( filter4['meta']['total_count'], 50 )
        
        # delete
        Profile.managers.delete()
        
        # read + compare
        self._read_all()
