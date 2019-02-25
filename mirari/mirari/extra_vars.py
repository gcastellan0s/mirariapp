FORMTEMPLATE1 = """
	<div class="m-portlet m-portlet--last m-portlet--head-lg m-portlet--responsive-mobile" id="main_portlet">
        {%if not 'FORM_BUTTONS' in model.VARS%}
            {%include 'generic/includes/create-update/generic_form_buttons.html'%}
        {%else%}
            {%if model.VARS.FORM_BUTTONS == 'TOP'%}
                {%include 'generic/includes/create-update/generic_form_buttons.html'%}
            {%endif%}
        {%endif%}
		<div class="m-portlet__body">
			<div class="m-portlet__body">
				<div class="m-form__content">
					{%for message in messages%}
						<div class="m-alert m-alert--icon alert alert-{{message.tags}}" role="{{message.tags}}">
							<div class="m-alert__icon">
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
							<div class="m-alert__text">
								{{message}}
							</div>
							<div class="m-alert__close">
								<button type="button" class="close" data-close="alert" aria-label="Close"></button>
							</div>
						</div>
					{%endfor%}
					<div class="m-alert m-alert--icon alert alert-danger m--hide" role="alert" id="form_msg">
						<div class="m-alert__icon">
							<i class="la la-warning"></i>
						</div>
						<div class="m-alert__text">
							Hay algúnos errores en tu formulario, corrigelos para poder continuar!
						</div>
						<div class="m-alert__close">
							<button type="button" class="close" data-close="alert" aria-label="Close"></button>
						</div>
					</div>
				</div>
"""

FORMTEMPLATE2 = """
			</div>
		</div>
        {%if 'FORM_BUTTONS' in model.VARS%}
            {%if model.VARS.FORM_BUTTONS == 'BOTTOM'%}
                {%include 'generic/includes/create-update/generic_form_buttons.html'%}
            {%endif%}
        {%endif%}
	</div>
"""