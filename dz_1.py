seconds = int(input('Введите число в секунад: '))
minutes = 0
hours = 0
days = 0

if seconds >= 60 and seconds < 3600:
    minutes = seconds // 60
    seconds %= 60
    print(minutes, 'мин', seconds, 'сек')


elif seconds >= 3600 and seconds < 86400:
    hours = seconds // 3600
    minutes = seconds // 60
    if minutes >= 60:
        minutes %= 60
        seconds %= 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')


elif seconds >= 86400:
    days = seconds // 86400
    hours = seconds // 3600
    minutes = seconds // 60
    if hours >= 24:
        hours %= 24
        if minutes >= 60:
            minutes %= 60
            seconds %= 60
    print(days, 'дни', hours, 'час', minutes, 'мин', seconds, 'сек')


else:
    print(seconds, 'сек')
