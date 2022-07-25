import re


def is_valid_time(time):
    # vaihtoehtoinen ^\d\d?:\d\d$
    time_regex = re.compile(r'\d\d?:\d{2}')
    match = time_regex.fullmatch(time)
    if match:
        return True
    else:
        return False


print(is_valid_time("2:30"))
print(is_valid_time("12:30"))
print(is_valid_time("112:30"))
print(is_valid_time("its a 15:30"))
print(is_valid_time("asdf22:30"))

print("------------bytes--------------")


def parse_bytes(data):
    parse_regex = re.compile(r'\b[0-1]{8}\b')
    match = parse_regex.findall(data)
    if match:
        return match
    else:
        return False


print(parse_bytes('10101011 0101 323'))
print(parse_bytes('my data is : 1010101012 110100101'))
print(parse_bytes('asksadf'))

print("------------dates--------------")


def parse_dates(date):
    date_regex = re.compile(r'(^\d\d)[,./](\d\d)[,./](\d{4}$)')
    match = date_regex.search(date)
    if match:
        dates_dict = {'d': match.group(1),
                      'm': match.group(2),
                      'y': match.group(3)}
        return dates_dict
    else:
        return None


print(parse_dates('a12,04,2003'))
print(parse_dates('312,04,2003'))
print(parse_dates('12,04,2003'))
print(parse_dates('12.04.2003'))
print(parse_dates('12/04/2003'))
print(parse_dates('12/04/2009345'))
print(parse_dates('12/as/2003345'))

print("------------dates--------------")


def censor(text):
    profanity_regex = re.compile(r'(\bfrack\w*\b)', re.I)
    result = profanity_regex.sub("CENSORED", text)
    return result


print(censor("fracking potato"))
print(censor("You fracker!"))
print(censor("Frack you"))
print(censor("sFrack you"))
print(censor("I hope you frackin fly"))
print(censor("Fracking frack"))
