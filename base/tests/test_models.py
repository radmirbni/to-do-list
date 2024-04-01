from django.test import TestCase

from base.models import Task

class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='some task')

    def test_title_label(self):
        task=Task.objects.get(id=1)
        field_label = task._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_title_name_max_length(self):
        task=Task.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEquals(max_length,200)

    def test_object_name_is_last_name_comma_first_name(self):
        task=Task.objects.get(id=1)
        expected_object_name = '%s' % (task.title)
        self.assertEquals(expected_object_name,str(task))

    def test_get_absolute_url(self):
        responce = self.client.get('/task-update/1/')
        self.assertEqual(responce.status_code, 302)