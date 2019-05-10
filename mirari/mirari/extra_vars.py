FORMTEMPLATE1 = """
	<div class="kt-portlet kt-portlet--last kt-portlet--head-lg kt-portlet--responsive-mobile" id="kt_page_portlet">
        {%if not 'FORM_BUTTONS' in model.VARS%}
            {%include 'generic/includes/create-update/generic_form_buttons.html'%}
        {%else%}
            {%if model.VARS.FORM_BUTTONS == 'TOP'%}
                {%include 'generic/includes/create-update/generic_form_buttons.html'%}
            {%endif%}
        {%endif%}
        <div class="kt-portlet__body">
            <div class="kt-form" id="kt_form">
                {%for message in messages%}
                    <div class="alert alert-danger fade show" role="alert">
                        <div class="alert-icon">
                            {%if message.tags == 'info'%}
                                <i class="la la-warning"></i>
                            {%elif message.tags == 'success'%}
                                <i class="la la-check"></i>
                            {%elif message.tags == 'warning'%}
                                <i class="la la-warning"></i>
                            {%elif message.tags == 'error'%}
                                <i class="la la-times"></i>
                            {%endif%}
                        </div>
                        <div class="alert-text">
                            {{message}}
                        </div>
                        <div class="alert-close">
                            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true"><i class="la la-close"></i></span>
                            </button>
                        </div>
                    </div>
                {%endfor%}
                <div class="kt-alert kt-alert--icon alert alert-danger kt-hide" role="alert" id="form_msg">
                    <div class="kt-alert__icon mr-3">
                        <i class="la la-warning"></i>
                    </div>
                    <div class="kt-alert__text">
                        Hay algúnos errores en tu formulario, corrigelos para poder continuar ! 
                    </div>
                    <div class="kt-alert__close">
                        <button type="button" class="close" data-close="alert" aria-label="Close"></button>
                    </div>
                </div>
            </div>
"""

FORMTEMPLATE2 = """
		</div>
        {%if 'FORM_BUTTONS' in model.VARS%}
            {%if model.VARS.FORM_BUTTONS == 'BOTTOM'%}
                {%include 'generic/includes/create-update/generic_form_buttons.html'%}
            {%endif%}
        {%endif%}
	</div>
"""