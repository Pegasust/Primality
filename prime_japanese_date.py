from find_next_prime import *
# all_prime_dates(1,0,2010,2100)
def get_first_day(year):
    year *= 10000
    year += 101
    return year

def get_last_day(year):
    year*= 10000
    year+= 1231
    return year

def year_str(n):
    date = n % 100
    n //= 100
    month = n % 100
    n //= 100
    return "{}/{}/{}".format(n,month,date)
    

def date_check(n, min_year = 1000, max_year = 2100):
    date = n % 100
    n//=100
    if date == 0 or date > 31:
        return False
    month = n % 100
    if month == 0 or month > 12:
        return False
    n//=100
    year = n
    if year < min_year or year > max_year:
        return False
    if month == 2:
        if year % 4 == 0:
            return date <= 29
        else:
            return date <= 28
    elif month <= 7:
        return date <= (31 if (month % 2) == 1 else 30)
    return date <= (31 if (month % 2) == 0 else 30)
    
def _next_prime_date(n=0, min_year=1000, max_year=2100):
    min_n = get_first_day(min_year)
    max_n = get_last_day(max_year)
    n = next_prime(max(n,min_n))
    while (not date_check(n, min_year, max_year)):
        if n > max_n:            
            return -1
        n = next_prime(n)
    return n

def next_prime_date(n=0, min_year=1000, max_year=2100):
    retval = _next_prime_date(n,min_year,max_year)
    if retval == -1:
        print("Couldn't find next prime date within year limit")
        return -1
    return retval

def all_prime_dates(year_gap, n=0, min_year = 1000, max_year=2100):
    year = min_year
    count = 0
    while year <= max_year:
        n = _next_prime_date(n, year, year)
        count += 1
        if n == -1:
            year += 1
            print("== Had {} prime dates.".format(count))
            count = 0
            print("===== YEAR {} =====".format(year))
            continue
        print("date:\t{}".format(year_str(n)))
        next_year = n//10000
        year = max(year + year_gap, next_year)
    print("Done")
