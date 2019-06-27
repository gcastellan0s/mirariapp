# -*- coding: utf-8 -*-
from django import template
from numbertoletters import number_to_letters
from money.money import Money
from money.currency import Currency

register = template.Library()

@register.filter
def addLinebreaks(string, number):
	c = 0
	for s in string:
		if c % number == 0 and c != 0: 
			string = string[0:c] + '<br />' + string[c:]
		c+=1
	return string

@register.filter
def numbertostring(number):
	number = number.split('.')
	return number_to_letters(number[0]) + ' pesos. ' + number[1] + '/100'

@register.filter
def iCat(string1, string2):
	return string1+'|'+string2

@register.filter
def MoneyMXN(number):
    try:
        return Money('{0:.2f}'.format(float(number)), Currency.MXN).format('es_MX')
    except:
        return number