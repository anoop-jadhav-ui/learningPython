# Write a Python script to find out what jobs you are qualified based on a set of skills.

# Define data science job roles and required skills
job_roles = [
    {'role': 'Data Analyst', 'skills': ['Python', 'SQL', 'Excel']},
    {'role': 'Data Scientist', 'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning']},
    {'role': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn']},
    {'role': 'Data Engineer', 'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL']},
    {'role': 'Business Intelligence Analyst', 'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel']},
    {'role': 'Quantitative Analyst', 'skills': ['R', 'Python', 'MATLAB', 'Statistics']},
    {'role': 'Operations Analyst', 'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement']},
    {'role': 'Database Administrator', 'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management']},
    {'role': 'AI Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision']},
    {'role': 'Statistician', 'skills': ['R', 'SAS', 'Python', 'Statistical Modeling']}
]
# My skills
my_skills = ['Python', 'SQL', 'Excel']

jobs = []

# Basic Solution
for job in job_roles:
  match = True
  
  for skill in my_skills:
    if skill not in job['skills']:
      match = False
  
  if match == True:
    jobs.append(job['role'])

print(jobs)

# Complex - all() method and list comprehension

jobs = []
for job in job_roles: 
  if all(skill in job['skills'] for skill in my_skills):
    jobs.append(job['role'])

print(jobs)