import re
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

ARTICLE_STATUS = (
    ("draft", _("Draft")),
    ("inprogress", _("In Progress")),
    ("published", _("Published")),
)


class UserProfile(AbstractUser):
    pass


class Article(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    content = models.TextField(_("Content"), blank=True, default="")
    word_count = models.IntegerField(_("Word Count"), blank=True, default="")
    twitter_post = models.TextField(_("Twitter Post"), blank=True, default="")
    status = models.CharField(
        _("Status"), max_length=20, choices=ARTICLE_STATUS, default="draft"
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name=_("Creator"),
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", "", self.content).replace("\n", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))

        super().save(*args, **kwargs)
