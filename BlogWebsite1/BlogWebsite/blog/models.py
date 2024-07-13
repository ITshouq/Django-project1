from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def str(self):
        return f"{self.id} {self.username} {self.email}"
class Category(models.Model):
        name = models.CharField(max_length=255, unique=True)

        def str(self):
            return self.name

class Post(models.Model):
            title = models.CharField(max_length=255)
            content = models.TextField()
            category = models.ForeignKey(Category, on_delete=models.CASCADE)
            date_published = models.DateField()

            def str(self):
             return f"{self.id} {self.title} {self.category} {self.date_published}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def str(self):
        return f"{self.user} {self.post} {self.date_posted}"