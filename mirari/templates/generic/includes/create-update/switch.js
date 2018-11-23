
$(".form-check").each(function (index) {
    label = $(this).children('label')
    hint = $(this).children('small')
    input = label.children('input')
    if (input.attr('class').includes("checkboxinput")) {
        text = label.text()
        parent = $(this).parent('div')
        parent.addClass('row')
        checked = ''
        if (input.is(':checked'))
            checked = 'checked="checked"'
        $(this).empty()
        $(this).append('<label class="col-12 col-form-label" for="' + input.attr('id') + '">' + text + '</label>')
        $(this).append('<div class="col-3"><span class="m-switch m-switch--outline m-switch--icon m-switch--primary"><label class="checkbox-container"><input type="checkbox" name="' + input.attr('name') + '" id="' + input.attr('id') + '" ' + checked + ' class="checkboxinput form-check-input"><span></span></label></div>')
        $(this).append(hint)
    }
});