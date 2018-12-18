FORM1PART = """
	<div class="m-portlet m-portlet--last m-portlet--head-lg m-portlet--responsive-mobile" id="main_portlet">
		<div class="m-portlet__head m-form__actions m-form__actions--solid">
			<div class="m-portlet__head-wrapper">
				<div class="m-portlet__head-caption">
					<div class="m-portlet__head-title">
						<a href="javascript:history.back(1)" class="btn btn-secondary m-btn m-btn--icon m-btn--wide m-btn--md m--margin-right-10">
                            <span>
                                <i class="la la-arrow-left"></i>
                                <span>REGRESAR</span>
                            </span>
                        </a>
					</div>
				</div>
				<div class="m-portlet__head-tools">
					{%include 'generic/includes/create-update/submit_buttons.html'%}
				</div>
			</div>
		</div>
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

FORM2PART = """
			</div>
		</div>
	</div>
"""