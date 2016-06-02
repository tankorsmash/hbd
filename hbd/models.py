from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User as djUser

class User(djUser):
	def __unicode__(self):
		return u"#{id}@{username} {firstname} {lastname}".format(
			id=self.id,
			username=self.username,
			firstname=self.first_name,
			lastname=self.last_name,
		)

# Create your models here.
class Birthday(models.Model):
	user = fields.related.OneToOneField(User)
	date = fields.DateField()


class Cheers(models.Model):
	"""each time you want to props someone for their birthday
	you create a Cheers object for it, the more times you cheers
	the more power you get.

	the more someone's birthday is cheersed, the more... happy they become
	"""

	#who we're cheersing
	target_user = fields.related.ForeignKey(User, related_name="cheers_to")
	#times its been cheersed
	count = fields.IntegerField(default=0)
	#people who have cheersed this user
	pals = fields.related.ManyToManyField(User, related_name="cheers_made")
