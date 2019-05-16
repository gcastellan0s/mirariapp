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
                    <div class="alert alert-{%if message.tags == 'error'%}danger{%else%}{{message.tags}}{%endif%} fade show mb-5" role="alert" id="form_msg">
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
                                <span aria-hidden="true">
                                    <i class="la la-close"></i>
                                </span>
                            </button>
                        </div>
                    </div>
                {%endfor%}
                <div class="alert alert-danger fade show kt-hide mb-5" role="alert" id="form_msg">
                    <div class="alert-icon"><i class="flaticon-warning"></i></div>
                    <div class="alert-text">Hay algúnos errores en tu formulario, corrigelos para poder continuar!</div>
                    <div class="alert-close">
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true"><i class="la la-close"></i></span>
                        </button>
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