"""
    This is the models.py for The_Xaming_Arena project
"""

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subject(models.Model):

    """
        Subject class contains all the entries for the subjects.
        Every Suject has a Subject name and also a Code name which
        is used to identify the subject uniquely.
    """

    code = models.CharField(_('code'), max_length=10, primary_key=True)
    name = models.CharField(_('name'), max_length=30)

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

    def __unicode__(self):
        return self.name


class Question(models.Model):

    """
        A 'Question' class is a template for a 'Question'.

        A Question has following properties...

        1. It has a subject code (to which subject it belongs to).
        2. It has a unique code to identify it in the database file.
        3. It has a text field to enter the question.
        4. It has four options.
        5. It may have descripiton, image, and date at which it entered.
    """

    subject_code = models.ForeignKey(Subject)
    question = models.CharField(_('question'), max_length=4000)

    A = models.CharField(_('A'), max_length=4000)
    B = models.CharField(_('B'), max_length=4000)
    C = models.CharField(_('C'), max_length=4000)
    D = models.CharField(_('D'), max_length=4000)

    description = models.CharField(_('description'),
                                   max_length=10000,
                                   blank=True)

    image = models.ImageField(_('image'),
                              upload_to="/static/image/",
                              blank=True)

    date_entered = models.DateTimeField(_('today date'),
                                        default=datetime.datetime.now)

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __unicode__(self):
        return "%s %s %s %s %s %s %s" % (self.id,
                                         self.subject_code,
                                         self.question,
                                         self.A,
                                         self.B,
                                         self.C,
                                         self.D)

ANSWER_CHOICES = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))


class Answer(models.Model):

    """It is a table which contains answers for each and every quesiton."""

    id = models.ForeignKey(Question, primary_key=True)
    answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')

    def __unicode__(self):
        return "%s, %s" % (self.id, self.answer)


class AbstractQuestionClass(models.Model):

    """This is a table which stores the details of the 10 questions."""

    one = models.IntegerField()
    two = models.IntegerField()
    three = models.IntegerField()
    four = models.IntegerField()
    five = models.IntegerField()
    six = models.IntegerField()
    seven = models.IntegerField()
    eight = models.IntegerField()
    nine = models.IntegerField()
    ten = models.IntegerField()

    class Meta:
        abstract = True


class ExamIdClass(AbstractQuestionClass):

    """This table contains exam ids."""

    id = models.AutoField(primary_key=True)


class AbstractAnswerClass(models.Model):

    """
        This is a Abstract class table which have details
        of the correct answers of every exam.
    """

    one = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    two = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    three = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    four = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    five = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    six = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    seven = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    eight = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    nine = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)
    ten = models.CharField(max_length=1,
                            choices=ANSWER_CHOICES)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s %s %s %s %s %s %s %s %s %s" % (self.one,
                                                    self.two,
                                                    self.three,
                                                    self.four,
                                                    self.five,
                                                    self.six,
                                                    self.seven,
                                                    self.eight,
                                                    self.nine,
                                                    self.ten)


class SubmittedAnswers(AbstractAnswerClass):

    """ This table contains submitted answers data"""

    id_exam = models.IntegerField()


class CorrectAnswers(AbstractAnswerClass):

    """ This table contais Correct answers data"""

    id_exam = models.IntegerField()


class Exam(models.Model):

    """
        This is a template for storing the details of a exam.

        This table have
                1. Exam id,
                2. User. i.e., the student name,
                3. to which subject the questions belongs to,
                4. marks obtained by the student,
                5. date of exam.
    """

    exam_id = models.IntegerField()
    user = models.CharField(max_length=30)
    subject = models.CharField(max_length=10)
    marks_obtained = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s %s %s" % (self.user, self.subject, self.marks_obtained)
