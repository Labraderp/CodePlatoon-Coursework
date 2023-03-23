from django.shortcuts import render
import random

# Create your views here.
users = {}

def index(request, id):
  if id in users:
    users[id]["count"] += 1
    response = render(request, "index.html", users[id])
    response.set_cookie(str(id), users[id], httponly=False, secure=False)
  else:
    rand_id = random.randint(1,10000)
    users[rand_id] = {
      "count" : 1
      }
    print(users)
    response = render(request, "index.html", users[rand_id])
    response.set_cookie(str(id), "new user", httponly=False, secure=False)
    
  
  return response