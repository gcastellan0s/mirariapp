$('#id_{{key}}').select2({
    ajax: {
        url: window.location.pathname,
        dataType: 'json',
        data: function (params) {
            return {
                search: params.term,
                field: '{{key}}',
                action: 'select2',
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