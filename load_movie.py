import os
import environ
import requests


env = environ.Env()
environ.Env.read_env('.env')
print('API_KEY: ', env('7c9f82c4bdd238bcffe74757df1c7bf5'))
print('API_TOKEN: ', env('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YzlmODJjNGJkZDIzOGJjZmZlNzQ3NTdkZjFjN2JmNSIsInN1YiI6IjY1Mjc4NDY0ZmQ2MzAwNWQ3YTJkMzI2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.go2c6UNVEoT2-J3FMTIv-Mqk1wZdZ3a1jyGFqkvEiqY'))

'''
url --request GET \
     --url 'https://api.themoviedb.org/3/movie/76341?language=en-US' \
     --header 'Authorization: Aasdfqwer' \
     --header 'accept: application/json'
'''
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {env('API_TOKEN')}"}

movie_id = 76341
r = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US', headers=headers) 
print(r.json())


r = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US', headers=headers) 
credits = r.json()
for actor in credits['cast'][:10]:
    print(actor['id'], actor['name'], actor['order'], actor['known_for_department'])

for job in credits['crew'][:15]:
    print(job['name'], job['department'], job['job'])