from django.db import models
from user.models import User
from problem.models import Problem
import django.utils.timezone as timezone
from submission.validator import validate_fetch_judge
from django.http import Http404

# Create your models here.

class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True, db_index=True)
    language = models.CharField(max_length = 64)
    problem = models.ForeignKey(Problem,on_delete = models.CASCADE , null = True)
    judge_status = models.CharField(max_length = 64)
    code = models.CharField(max_length=65535 , blank = True )
    submit_time = models.DateTimeField( 'Submit time' , null = True , default = timezone.now )
    user = models.ForeignKey(User,on_delete = models.CASCADE , null = True)
    class Meta:
        ordering = ['-submission_id']

    class Judge:
        field = ['submission_id' , 'language' , 'problem' , 'code' ]
        problem_field = [ 'time_limit' , 'memory_limit' , 'checker' ]
        ignore_field = [ 'complete' ]

    def get_problem_field( self , dic ):
        for _ in self.Judge.problem_field:
            dic[_] = getattr( self.problem , _ )
    
            
def get_update_field( dic ):
    for _ in Submission.Judge.ignore_field:
        dic.pop( _ )
    return dic

class Judgeinfo(models.Model):
    judgeinfo_id = models.AutoField(primary_key=True, db_index=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE )
    result = models.CharField( max_length = 64 , default = '' )
    time_cost = models.CharField( max_length = 12 )
    memory_cost = models.CharField( max_length = 12 )
    additional_info = models.CharField( max_length = 512 )
    case = models.SmallIntegerField( null = True , editable = False )

    def __str__(self):
        return str(self.judgeinfo_id)
    
    class Meat:
        ordering = ['case']


def validator_fetch_judge( function ):
    def wrapper( * argv , ** kw ):
        try:
            if validate_fetch_judge( argv[0] ) == False:
                raise PermissionError()
        except PermissionError:
            raise Http404( 'Permission Denied' )
        except:
            raise Http404( 'Unknown Error' )
        return function( * argv , ** kw )
    return wrapper