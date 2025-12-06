from datetime import datetime, timedelta
from sqlite3 import IntegrityError
from django.utils import timezone
from decimal import Decimal

from appointment.models import *
from cabin.models import *
from cabin_bill.models import *
from cabin_history.models import *
from cashier.models import *
from doctor.models import *
from duty_schedule.models import *
from duty_shift.models import *
from emergency.models import *
from it_member.models import *
from mats.models import *
from medical_test.models import *
from medicine_bill.models import *
from nurse.models import *
from pathologist.models import *
from patient.models import *
from prescription.models import *
from staff.models import *
from store_medicine.models import *
from test_bill.models import *
from test_history.models import *
from test_report.models import *

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from functools import wraps
from django.contrib import messages  
from django.db.models import Q, Avg, Count, Sum, F, ExpressionWrapper, DecimalField
from django.core.exceptions import FieldError
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')