$('#id_{{key}}').select2({
    ajax: {
        url: {%block select2url%}window.location.pathname{%endblock select2url%},
        dataType: 'json',
        data: function (params) {
            return {
                search: params.term,
                field: '{{key}}',
                action: 'select2',
                {%for field_filter in value.field_filter%}
                    {{field_filter.0}}:{{field_filter.1|safe}},
                {%endfor%}
            }
        },
        processResults: function (data, params) {
            return {
                results: data.items,
            };
        },
        cache: true
    },
    escapeMarkup: function (markup) { return markup; },
    minimumInputLength: 1,
    templateResult: formatRepo,
    templateSelection: formatRepoSelection,
    {%if value.placeholder%}
        placeholder: '{{value.placeholder}}',
    {%endif%}
    language: 'es',
});