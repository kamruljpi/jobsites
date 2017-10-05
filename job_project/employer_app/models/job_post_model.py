from django.db import models


# Create your models here.
class JobPost(models.Model):
  #Account Information
  company = models.ForeignKey("employer_app.Employer", on_delete=models.CASCADE, null=True)
  category = models.ForeignKey("jobpost_app.Category", on_delete=models.CASCADE, null=True)
  industry = models.ForeignKey("jobpost_app.Industry", on_delete=models.CASCADE, null=True)
  job_title = models.CharField(max_length=200, default="", null=True)
  vacancies = models.IntegerField(default=1)
  with_photo = models.BooleanField(default=True)
  apply_ins = models.CharField(max_length=500, default="", null=True)
  last_date = models.DateTimeField(null=True)
  age_range_form = models.IntegerField(null=True)
  age_range_to = models.IntegerField(null=True)
  gender = models.IntegerField(null=True)
  job_type = models.IntegerField(null=True)
  job_level = models.IntegerField(null=True)
  edu_qualification = models.CharField(max_length=500, default="", null=True)
  job_context = models.CharField(max_length=500, default="", null=True)
  job_resp = models.CharField(max_length=500, default="", null=True)
  adtn_job_requirements = models.CharField(max_length=500, default="", null=True)
  adtn_job_req = models.CharField(max_length=500, default="", null=True)
  exp_type = models.IntegerField(null=True)
  exp_min = models.IntegerField(null=True)
  exp_max = models.IntegerField(null=True)
  location = models.ForeignKey("jobpost_app.Location", on_delete=models.CASCADE, null=True)
  salary_range_flag = models.IntegerField(null=True)
  salary_min = models.IntegerField(null=True)
  salary_max = models.IntegerField(null=True)
  other_benefits = models.CharField(max_length=500, default="", null=True)
  excl_job_flag = models.IntegerField(null=True)
  create_by = models.CharField(max_length=20, default="")
  create_date = models.DateTimeField(auto_now_add=True, null=True)
  update_by = models.CharField(max_length=20, default="")
  update_date = models.DateTimeField(auto_now=True, null=True)
  active = models.BooleanField(default=True)