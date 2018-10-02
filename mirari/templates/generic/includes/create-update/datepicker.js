$(".dateinput").datepicker({
    format: "dd/mm/yyyy",
    todayHighlight: !0,
    templates: {
        leftArrow: '<i class="la la-angle-left"></i>',
        rightArrow: '<i class="la la-angle-right"></i>'
    },
});
$(".datetimeinput").datetimepicker({
    todayHighlight: !0,
    autoclose: !0,
    format: "dd/mm/yyyy hh:ii"
})