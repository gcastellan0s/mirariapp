{%load static%}
{%load i18n%}

Vue.component('date-picker', {
    mounted: function () {
        $(this.$el).bootstrapMaterialDatePicker(
            {format : 'DD/MM/YYYY HH:mm',minDate : new Date(),lang: 'es-mx',cancelText: 'CANCELAR',switchOnClick : true}
        ).on('change', function(e, date){
            self.Ticket.datetimeOfDelivery = self.$options.filters.FormatTDate(date.format()) 
        });
    },
    template: '<input/>',
});