from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


class TaskList(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='admin',password='123')
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data, {'id':1,'username':'admin','tasks':[]}
        )

    def test_post(self):
        response = self.client.post('/api/tasks/',{'title':'test task','description':'Rustam'},format='json')
        self.assertEqual(response.status_code,200)
