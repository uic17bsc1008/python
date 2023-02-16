from django.db import models
# from questions.models import Question

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)
class Quiz(models.Model):
    name = models.CharField(max_length=120) 
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quize in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]
    
    class Meta:
        verbose_name_plural = 'Quizes'

