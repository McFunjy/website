from django.test import TestCase
from posts.models import Post


class TaskModeTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Post.objects.create(
             text='Hello',
             author='admin'
         )
        cls.task = Post.objects.get(text='Hello')



    def test_title_label(self):
        """verbose_name поля text совпадает с ожидаемым"""
        task = TaskModeTest.task
        verbose = task.meta.get_field('text').verbose_name
        self.assertEquals(verbose, 'Текст поста')