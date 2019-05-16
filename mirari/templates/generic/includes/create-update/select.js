{%include 'generic/includes/create-update/select2-es.js' with key=key value=value%}
///////SELECT

$(".select").each(function(i) {
    $(this).removeClass('select')
    $(this).addClass('m-select2')
});

$('.m-select2').select2({
    //placeholder: "Elige 1 opción",
    // minimumResultsForSearch: -1
});

{%for key, value in model.VARS.SELECTQ.items%}
    {%if value.plugin == 'select2'%}
        {%if value.sercheable%}
            {%include 'generic/includes/create-update/searchselect2.js' with key=key value=value%}
        {%else%}
            $('#id_{{key}}').select2();
        {%endif%}
    {%elif value.plugin == 'selectmultiple'%}
        {%include 'generic/includes/create-update/selectmultiple.js' with key=key value=value%}
    {%endif%}
{%endfor%}
function formatRepo (repo) {
    if (repo.loading) {
        return 'Buscando coincidencias';
    }
    return repo.str_select2;
}
function formatRepoSelection (repo) {
    return repo.str_select2 || repo.text;
}