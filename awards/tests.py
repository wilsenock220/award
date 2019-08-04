from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Profile

class ProjectTestCases(TestCase):
    def setUp(self):
        self.new_project = Project(id=1,screenshot='media/Nature.jpg',title='Pitch', url='https://nimo-pitch.herokuapp.com',description='Test',created_on='15-03-2019')
        self.new_project.save_project()

    def tearDown(self):
        Project.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_method(self):
        self.new_project.save_project()
        all_obj = Project.objects.all()
        self.assertTrue(len(all_obj)>0)

    def test_delete_method(self):
        self.new_project.save_project()
        obj_filt = Project.objects.filter(proj_title='Nature')
        Project.delete_project(obj_filt)
        obj_all = Project.objects.all()
        self.assertTrue(len(obj_all) == 0)

class ProfileTestCases(TestCase):
    def setUp(self):
        self.new_profile = Profile(id=1, profile_pic='media/profile/mypic.jpg', bio='Live life',
                                   projects_id='1', telephone='07190000', full_name='Wairimu Maina')


    def tearDown(self):
        Profile.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        all_obj = Profile.objects.all()
        self.assertTrue(len(all_obj) > 0)

