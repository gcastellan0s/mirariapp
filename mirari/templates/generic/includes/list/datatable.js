{% load static %}
{% load i18n %}
{% load mirari_tags %}
var options = {
    data: {
        type: 'remote',
        source: {
            read: {
                url: '',
                method: 'GET',
                params: {
                    action: 'list',
                },
                map: function(raw) {
                    var dataSet = raw;
                    console.log(raw)
                    if (typeof raw.data !== 'undefined') {
                        dataSet = raw.data;
                    }
                    return dataSet;
                },
            }
        },
        pageSize: {{paginator_size}},
        saveState: {
            cookie: false,
            webstorage: false
        },
        serverPaging: true,
        serverFiltering: true,
        serverSorting: true,
    },
    layout: {
        theme: 'default',
        class: 'm-datatable--brand',
        scroll: false,
        height: null,
        footer: false,
        header: true,
        smoothScroll: {
            scrollbarShown: true
        },
        spinner: {
            overlayColor: '#000000',
            opacity: 0,
            type: 'loader',
            state: 'brand',
            message: true
        },
        icons: {
            sort: {
                asc: 'la la-arrow-up',
                desc: 'la la-arrow-down'
            },
            pagination: {
                next: 'la la-angle-right',
                prev: 'la la-angle-left',
                first: 'la la-angle-double-left',
                last: 'la la-angle-double-right',
                more: 'la la-ellipsis-h'
            },
            rowDetail: {
                expand: 'fa fa-caret-down',
                collapse: 'fa fa-caret-right'
            }
        }
    },
    sortable: true,
    pagination: true,
    search: {
        onEnter: false,
        input: $('#generalSearch'),
        delay: 400,
    },
    rows: {
        callback: function() {},
        autoHide: false,
    },
    columns: {{list | safe | datatableformat}},
    toolbar: {
        layout: ['pagination', 'info'],
        placement: ['bottom'],
        items: {
            pagination: {
                type: 'default',
                pages: {
                    desktop: {
                        layout: 'default',
                        pagesNumber: 6
                    },
                    tablet: {
                        layout: 'default',
                        pagesNumber: 3
                    },
                    mobile: {
                        layout: 'compact'
                    }
                },
                navigation: {
                    prev: true,
                    next: true,
                    first: true,
                    last: true
                },
                pageSizeSelect: [10, 20, 30, 50, 100]
            },
            info: true
        }
    },
    translate: {
        records: {
            processing: 'Espere ...',
            noRecords: 'No se encontraron regsitros'
        },
        toolbar: {
            pagination: {
                items: {
                    default: {
                        first: 'Primero',
                        prev: 'Anterior',
                        next: 'Siguiente',
                        last: 'Anterior',
                        more: 'Más páginas',
                        input: 'Numero',
                        select: 'Registros por página'
                    },
                    {% verbatim %}
                        info: 'Mostrando {{start}} a {{end}} de {{total}} registros'
                    {% endverbatim %}
                }
            }
        }
    },
}
var datatable{{model.VARS.MODEL}} = $('#m_datatable{{model.VARS.MODEL}}').mDatatable(options);
$("#m_datatable{{model.VARS.MODEL}}").on("change", function() {
    self.selected_items = datatable{{model.VARS.MODEL}}.rows(".m-datatable__row--active").nodes().find('.m-checkbox--single > [type="checkbox"]').length
})