from unicodedata import category
from django.test import TestCase

from third_eye_app.models import Business, Profile_thirdeye, User_Posts

# Create your tests here.

# profile test
def profile_test():
    def setup(self):
        self.new_profile=Profile_thirdeye(name="Test", email="test@gmail.com", bio="My test bio", profile_picture="image.jpg", phone_number="0759700444")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile_thirdeye))

    
    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile_thirdeye.objects.all()
        self.assertTrue(len(profiles)>0)


def business_test():
    def setup(self):
        self.new_business=Business(name="biz", email="biz@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_save_business(self):
        self.new_business.save_business()
        businesses=Business.objects.all()
        self.assertTrue(len(businesses)>0)

def User_Posts_test():
    def setup(self):
        self.new_User_Post = User_Posts(category='test', content='The following is a test to confirm if test category is working')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_User_Post, User_Posts))

    def test_save_posts(self):
        self.new_User_Post.save_User_Posts()
        post = User_Posts.objects.all()
        self.assertTrue(len(post))