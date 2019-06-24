from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Thread


class ThreadTestCase(TestCase):
	def setUp(self):
		self.user1 = User.objects.create_user('usuario1', 'usuario1@test.com', 'testpwd123')
		self.user2 = User.objects.create_user('usuario2', 'usuario2@test.com', 'testpwd123')
		self.user3 = User.objects.create_user('usuario3', 'usuario3@test.com', 'testpwd123')
		self.thread = Thread.objects.create()

	def test_add_users_to_thread(self):
		self.thread.users.add(self.user1, self.user2)
		self.assertEqual(len(self.thread.users.all()), 2)

	def test_filter_thread_by_user(self):
		self.thread.users.add(self.user1, self.user2)
		threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
		self.assertEqual(self.thread, threads[0])

	def test_filter_non_existent_thread(self):
		threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
		self.assertEqual(len(threads), 0)

	def test_add_message_to_thread(self):
		self.thread.users.add(self.user1, self.user2)
		message1 = Message.objects.create(user=self.user1, content="Mensaje de prueba")
		message2 = Message.objects.create(user=self.user2, content="Contestación de prueba")
		self.thread.messages.add(message1, message2)
		self.assertEqual(len(self.thread.messages.all()), 2)

		for message in self.thread.messages.all():
			print("({}): {}".format(message.user, message.content))

	def test_add_message_from_user_not_in_thread(self):
		self.thread.users.add(self.user1, self.user2)
		message = Message.objects.create(user=self.user3, content="Mensaje de prueba")
		self.thread.messages.add(message)
		self.assertEqual(len(self.thread.messages.all()), 0)

	def test_find_thread_with_custom_manager(self):
		self.thread.users.add(self.user1, self.user2)
		thread = Thread.objects.find(self.user1, self.user2)
		self.assertEqual(self.thread, thread)

	def test_find_or_create_thread_with_custom_manager(self):
		self.thread.users.add(self.user1, self.user2)
		thread = Thread.objects.find(self.user1, self.user2)
		self.assertEqual(self.thread, thread)
		thread = Thread.objects.find_or_create(self.user1, self.user3)
		self.assertIsNotNone(thread)
