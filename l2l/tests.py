from django.test import TestCase

# Create your tests here.
#
# Cases I would test
# 1) Accurately changes a date to a string
# now = datetime.now()
# iso = now.strftime("%Y-%m-%dT%H:%M:%S")
# <p class="lead fw-normal">Today's date from a date is: {{ now|l2l_dt }}</p>

# 2) Accurately changes string to date
# <p class="lead fw-normal">Today's date from a string is: {{ iso|l2l_dt }}</p>

# 3) A datetime object that can't be formatted will print "Datetime object cannot be formatted". This shouldn't be able to happen with datetime.now()

# 4) A string that can't be formatted as a date will print "String object cannot be converted to datetime'
# string = 'hello there'
# <p class="lead fw-normal">Today's date from a string is: {{ string|l2l_dt }}</p>
