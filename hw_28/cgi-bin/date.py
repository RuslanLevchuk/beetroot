#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
vrem = datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d")
# служебные заголовки
print("Content-type: text/html")
print()
# содержимое сайта
print('''
<!DOCTYPE html>
<html class="client-nojs" lang="ru" dir="ltr">
<head>
<meta charset="UTF-8"/>''')
print('''
<body>
<html>''')
print('<a href="../">Головна</a>')
print('<title>Дата і час</title>')
print(f'<h1>Поточний час:</h1>')
print(f'<p>{vrem}</p>')
print('''
<body/>
<html/>''')

