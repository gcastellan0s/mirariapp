{% load static %}
{% load i18n %}
{% load mirari_tags %}

"use strict";
var KTDatatablesDataSourceAjaxServer = function() {
	var initTable1 = function() {
		var table = $('#kt_table_{{model.VARS.MODEL}}');
		table.DataTable({
			responsive: true,
			searchDelay: 500,
			processing: true,
			serverSide: true,
            language: {
                'url':'//cdn.datatables.net/plug-ins/1.10.19/i18n/Spanish.json'
            },
            searchDelay: 500,
            ajax: {
                url: '',
                type: 'GET',
                data: function (d) {
                    d.action = 'list'
                    {% for item in filters %}
                        d.{{item.key}} = $("#m_form_{{item.key}}").val()
                    {% endfor %}
                },
            },
            dom:
				"<'row'<'col-sm-12'tr>>" +
				"<'row'<'col-sm-12 col-md-4'p><'col-sm-12 col-md-2'l><'col-sm-12 col-md-6'i>>",
			columnDefs: [
                {% for item in list %}
                    {
                        targets: {{forloop.counter0}},
                        data: '{{item.field}}',
                        title: '{{item.title|upper}}',
                        orderable: {{item.sortable}},
                        {%if item.className%}
                            className: '{{item.className}}',
                        {%endif%}
                        {%if item.width%}
                            width: '{{item.width}}px',
                        {%endif%}
                        {%if item.template%}
                            render: function(data, type, full, meta) {
                                return `{{item.template|safe|renderDataTable}}`;
                            },
                        {%endif%}
                },
                {% endfor %}
			],
		});
        $('#generalSearch').on('keyup',function(){$('#kt_table_{{model.VARS.MODEL}}').DataTable().search(this.value,).draw()});
        {% for item in filters %}
            $("#m_form_{{item.key}}").selectpicker()
            $("#m_form_{{item.key}}").on("change", function() {
                $('#kt_table_{{model.VARS.MODEL}}').DataTable().draw()
            })
        {% endfor %}
	};
	return {
		init: function() {
			initTable1();
		},
	};
}();
jQuery(document).ready(function() {
	KTDatatablesDataSourceAjaxServer.init();
});