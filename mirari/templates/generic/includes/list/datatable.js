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
            {%if not SORTEABLE in model.VARS%}
                ordering: false,
            {%endif%}
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
				"<'row'<'col-sm-12 col-md-4'p><'col-sm-12 col-md-2 mt-2'l><'col-sm-12 col-md-6'i>>",
            {%if 'select' in list.0%}
                headerCallback: function(thead, data, start, end, display) {
                    thead.getElementsByTagName('th')[0].innerHTML = `
                        <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid kt-checkbox--brand">
                            <input type="checkbox" value="" class="kt-group-checkable">
                            <span></span>
                        </label>`;
                },
            {%endif%}
			columnDefs: [
                {% for field in list %}
                    {%if 'select' in field%}
                        {
                            targets: {{forloop.counter0}},
                            title: '{{field.title|upper}}',
                            orderable: false,
                            {%if field.width%}
                                width: '{{field.width}}px',
                            {%endif%}
                            render: function(data, type, row, meta) {
                                return `
                                <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid kt-checkbox--brand">
                                    <input type="checkbox" value="" delete="${row.property_url_delete}" class="kt-checkable">
                                    <span></span>
                                </label>`;
                            },
                        },
                    {%else%}
                        {
                            targets: {{forloop.counter0}},
                            title: '{{field.title|upper}}',
                            data: '{{field.field}}',
                            orderable: {%if field.sortable == 'false'%}false{%else%}true{%endif%},
                            {%if field.width%}
                                width: '{{field.width}}px',
                            {%endif%}
                            {%if field.className%}
                                className: '{{field.className}}',
                            {%endif%}
                            {%if field.template%}
                                render: function (data, type, row, meta) {
                                    return `{{field.template|safe|renderDataTable}}`
                                },
                            {%endif%}
                        },
                    {%endif%}
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
        table.on('change', '.kt-group-checkable', function() {
			var set = $(this).closest('table').find('.kt-checkable');
			var checked = $(this).is(':checked');
			$(set).each(function() {
				if (checked) {
					$(this).prop('checked', true);
					//$('#kt_table_{{model.VARS.MODEL}}').DataTable().rows($(this).closest('tr')).select();
				}
				else {
					$(this).prop('checked', false);
					//$('#kt_table_{{model.VARS.MODEL}}').DataTable().rows($(this).closest('tr')).deselect();
				}
			});
		});
        $('#kt_table_{{model.VARS.MODEL}}').on("change", function() {
            self.selected_items = $(this).closest('table').find('.kt-checkable:checked').length
        })
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