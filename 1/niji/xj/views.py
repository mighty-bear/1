from django.shortcuts import render
from django.shortcuts import render, redirect
from docx.api import Document
import pymysql
from .models import *
from niji import models as md
import re
from django.contrib.auth.models import User
from docx import Document
from fuzzywuzzy import fuzz


# Create your views here.

def index(request):
    return render(request, 'test.html')


def LiHe(request):
    return render(request, '李贺.html')
