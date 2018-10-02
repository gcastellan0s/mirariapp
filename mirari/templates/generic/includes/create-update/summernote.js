var Summernote = {
    init: function () {
        {%for summernote in  model.VARS.SUMMERNOTE%}
            $("#id_{{summernote}}").summernote({
                height: 200
            })
        {%endfor%}
    }
};
jQuery(document).ready(function () {
    Summernote.init()
});