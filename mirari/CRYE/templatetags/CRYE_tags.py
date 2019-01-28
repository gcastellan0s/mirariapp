# -*- coding: utf-8 -*-
from django import template
from mirari.mirari.vars import *
from mirari.mirari.models import *
from django.conf import settings

import urllib.request
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def get_TASAS(user):
	soup = BeautifulSoup(urllib.request.urlopen('http://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CF101&sector=18&locale=es').read().decode(u'latin-1'))
	titleshtml = soup.findAll("table", { "id" : "tablaTitulos" })
	titles = []
	for t in titleshtml[0].findAll('td'):
		titles.append(t.text.replace('  ','').replace('\n','').replace('\t','').replace('\r',''))
	descriptions = []
	for d in soup.findAll("td", { "class" : "tdDescripcion" }):
		descriptions.append(d.get_text().replace('  ','').replace('\n','').replace('\t','').replace('\r','').replace('/','').encode('latin-1'))
	tablaObservaciones = soup.findAll("table", { "id" : "tablaObservaciones" })
	valores = []
	for table in tablaObservaciones:
		td = table.findAll('td')
		cantidades = []
		for t in td:
			cantidades.append(t.text.replace('  ','').replace('\n','').replace('\t','').replace('\r',''))
		valores.append(cantidades)
	print(valores)
	html = ("""
		<table class="table table-striped- table-bordered table-hover table-checkable" id="m_table_1">
			<thead>
				<tr>
					<th title="Field #1" data-field=""></th>
					<th title="Field #2" data-field="">{0}</th>
					<th title="Field #3" data-field="">{1}</th>
					<th title="Field #3" data-field="">{2}</th>
				</tr>
			</thead>
			<tbody>
		""").format(titles[0],titles[1],titles[2])
	count = 0
	for description in descriptions:
		html += ("""
			<tr>
				<td>{0}</td>
				<td>{1}</td>
				<td>{2}</td>
				<td>{3}</td>
			</tr>
		""").format(description.decode('latin-1'), valores[count][0], valores[count][1], valores[count][2])
		count+=1
	html += """ 
			</tbody>
		</table>
	"""
	return html