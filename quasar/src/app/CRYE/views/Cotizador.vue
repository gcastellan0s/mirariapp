<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      <span class="text-muted font-weight-light">COTIZADOR /</span> ARRENDAMIENTO PURO
    </h4>
    <b-card header="DATOS DEL CLIENTE" header-tag="h6" class="mb-4">
      <div class="demo-vertical-spacing-sm">
        <b-form-group label="Cliente">
          <b-input type="text" placeholder="Nombre del cliente" v-model="cotizador.cliente"/>
        </b-form-group>
        <b-form-group label="Bien que cotiza">
          <b-input type="text" placeholder="Descripción del bien" v-model="cotizador.bien"/>
        </b-form-group>
      </div>
    </b-card>
    <div class="row">
      <div class="col-sm-6 col-xl-6">
        <b-card header="INFORMACIÓN" header-tag="h6" class="mb-4">
          <div class="demo-vertical-spacing-sm">
            <b-form-group label="Valor total">
              <b-input-group prepend="$">
                <b-input type="number" placeholder="Valor total con iva" v-model="cotizador.valor"/>
              </b-input-group>
            </b-form-group>
            <b-form-group label="Plazo">
              <NumberInputSpinner
              :min="1"
              :max="100"
              inputClass="form-control"
              buttonClass="btn btn-secondary"
              :integerOnly="true"
              v-model="cotizador.plazo" />
            </b-form-group>
            <b-form-group label="Fecha de inicio">
              <datepicker
              v-model="cotizador.fecha"
              :language="es"
              :bootstrapStyling="true"
              :monday-first="true"
              :full-month-name="true"
              placeholder="Select arrival date"
              :calendar-button="true"
              calendar-button-icon="ion ion-md-calendar"
              :clear-button="true"
              :disabled-dates="disabledDates"/>
            </b-form-group>
            <!-- Features -->
          </div>
        </b-card>
      </div>
      <div class="col-sm-6 col-xl-6">
        <b-card header="VALORES" header-tag="h6" class="mb-4">
          <div class="row">
            <div class="col-sm-6 col-xl-6">
              <div class="demo-vertical-spacing-sm">
                <b-form-group label="TIIE">
                  <b-input v-model="cotizador.tiie" type="text" placeholder=""/>
                </b-form-group>
              </div>
            </div>
            <div class="col-sm-6 col-xl-6">
              <div class="demo-vertical-spacing-sm">
                <b-form-group label="PUNTOS">
                  <b-input v-model="cotizador.puntos" type="text" placeholder=""/>
                </b-form-group>
              </div>
            </div>
          </div>
        </b-card>
      </div>
      <div class="col-xl-12">
        <b-card no-body class="mb-4">
          <b-card-header header-tag="h6" class="with-elements">
            <div class="card-header-title">TABLA DE RENTAS</div>
            <div class="card-header-elements ml-auto">
              <b-btn variant="default" class="btn-xs md-btn-flat">IMPRIMIR</b-btn>
            </div>
          </b-card-header>
          <b-card-body>
            <div class="rounded ui-bordered p-3 mb-3">
              <div class="text-muted small text-nowrap float-right">Unión de Crédito Credipyme, S.A. de C.V. CDMX a {{hoy}}</div>
              <div class="media align-items-center mt-3 mb-4">
                <img :src="M.LOGOBG" class="d-block ml-5" alt style="max-width:250px;">
              </div>
              <div class="row p-3">
                <div class="col-sm-4 col-xl-4">
                  CLIENTE: <strong>{{cotizador.cliente | ifnot}}</strong>
                  <br />
                  BIEN: <strong>{{cotizador.bien | ifnot}}</strong>
                </div>
              </div>
              <div class="row p-3">
                <div class="col-sm-4 col-xl-4">
                  VALOR TOTAL: <strong>{{cotizador.valor | currency | ifnot }}</strong>
                  <br />
                  VALOR SIN I.V.A.: <strong>{{ valor_sin_iva() | currency | ifnot }}</strong>
                  <br />
                  I.V.A.: <strong>{{iva() | currency | ifnot }}</strong>
                  <br />
                  PAGO INICIAL: <strong>{{pago_inicial() | currency | ifnot}}</strong>
                  <br />
                  TOTAL A FINANCIAR: <strong>{{total_a_financiar() | currency | ifnot}}</strong>
                  <br />
                  COMISION POR APERTURA: <strong>{{ comision_por_apertura() | currency | ifnot}}</strong>
                  <br />
                  IVA TOTAL: <strong>{{ iva_total() | currency | ifnot}}</strong>
                  <br/>
                  DESEMBOLSO INICIAL: <strong>{{ desembolso_incial() | currency | ifnot}}</strong>
                </div>
                <div class="col-sm-4 col-xl-4">
                  NUMERO DE UNIDADES: <strong>{{cotizador.unidades | ifnot}}</strong>
                  <br />
                  PLAZO A MESES: <strong>{{cotizador.plazo | ifnot}}</strong>
                  <br />
                  FECHA DE INICIO: <strong>{{cotizador.fecha | ffecha | ifnot}}</strong>
                  <br />
                  FECHA DE PRIMER PAGO: <strong>{{fecha_primer_pago() | ffecha | ifnot}}</strong>
                </div>
                <div class="col-sm-4 col-xl-4">
                  PLAZO: <strong>{{cotizador.plazo | ifnot}}</strong>
                  <br />
                  TASA ANUAL SIN I.V.A.: <strong>{{tasa_anual_sin_iva()| ifnot}}%</strong>
                  <br />
                  TIIE:<strong> {{cotizador.tiie | ifnot}}</strong>
                  <br />
                  PUNTOS: <strong>{{cotizador.puntos | ifnot}}</strong>
                  <br />
                  TASA: <strong>{{tasa() | ifnot}}</strong>
                </div>
              </div>
            </div>
          </b-card-body>
          <div class="table-responsive mb-5">
            <table class="table card-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>SALDO INSOLUTO</th>
                  <th>RENTA</th>
                  <th>IVA RENTA</th>
                  <th>RENTA TOTAL</th>
                  <th>FECHA DE VENCIMIENTO</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="index in num_plazos()" :key="index">
                  <td>{{index}}</td>
                  <td>{{saldo(index, renta_total(renta(index),iva_renta(renta(index))))| currency}}</td>
                  <td>{{renta(index)| currency}}</td>
                  <td>{{iva_renta(renta(index))| currency}}</td>
                  <td>{{renta_total(renta(index),iva_renta(renta(index)))| currency}}</td>
                  <td>{{fecha_tabla(index)|ffecha}}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="text-muted small text-nowrap float-left ml-3"> *La póliza que ampara el seguro del bien, será contratada por el cliente por la vigencia del arrendamiento  a nombre de Unión de Crédito Credipyme, S.A. de C.V.</div>
          <div class="text-muted small text-nowrap float-left ml-3"> **Esta cotización tiene una vigencia de 30 días naturales a partir de su expedición</div>
          <div class="text-muted small text-nowrap float-left ml-3 mb-5"> ***Estas condiciones solo son informativas y no aplica compromiso alguno por parte de Unión de crédito Credipyme S.A. de C.V. ya que esta sujeta a la aprobación correspondiente</div>
        </b-card>  
      </div>
    </div>
  </div>
</template>
<style src="@appwork/vendor/libs/vuejs-datepicker/vuejs-datepicker.scss" lang="scss"></style>
<style src="@appwork/vendor/libs/vue-number-input-spinner/vue-number-input-spinner.scss" lang="scss"></style>
<script>
import moment from 'moment'
import Datepicker from 'vuejs-datepicker'
import {en, es} from 'vuejs-datepicker/dist/locale'
import NumberInputSpinner from 'vue-number-input-spinner'
export default {
  name: 'forms-extras',
  metaInfo: {
      title: require('@/../../package.json').title,
      titleTemplate: '%s :: ' + require('@/../../package.json').slogan
  },
  components: {
    Datepicker,
    NumberInputSpinner,
  },
  data: () => ({
    hoy: moment().format("DD/MM/YY"),
    cotizador:{
      cliente:'',
      bien:'',
      tiie:8.1038,
      puntos:16.0,
      valor:0,
      plazo:1,
      iva: .16,
      fecha: moment().toDate(),
      unidades: 1,
      numbers: [ 1, 2, 3, 4, 5 ],
    },
    disabledDates: {
      to: moment().toDate(),  
    },
    es: es,
  }),
  methods: {
    fecha_primer_pago: function (value) {
      return moment(value).add(1, 'M');
    },
    fecha_tabla: function (index) {
      return moment(this.fecha_primer_pago()).add(index, 'M');
    },
    valor_sin_iva: function (value) {
      return this.cotizador.valor / 1.16
    },
    iva: function (value) {
      return this.cotizador.valor-this.valor_sin_iva()
    },
    pago_inicial: function (value) {
      return this.valor_sin_iva()*.2
    },
    total_a_financiar: function (value) {
      return this.valor_sin_iva()-this.pago_inicial()
    },
    comision_por_apertura: function (value) {
      return this.total_a_financiar()*.02
    },
    iva_total: function (value) {
      return (this.comision_por_apertura()+this.pago_inicial())*.16
    },
    desembolso_incial: function (value) {
      return this.pago_inicial()+this.comision_por_apertura()+this.iva_total()
    },
    tasa_anual_sin_iva: function (value) {
      return ((this.cotizador.tiie+this.cotizador.puntos)*100).toFixed(4)
    },
    tasa: function (value) {
      return this.cotizador.tiie+this.cotizador.puntos
    },
    num_plazos: function (value) {
      return this.cotizador.plazo
    },
    pmt: function (ir, np, pv, fv, type) {
      var pmt, pvif;
      fv || (fv = 0);
      type || (type = 0);
      if (ir === 0)
          return -(pv + fv)/np;
      pvif = Math.pow(1 + ir, np);
      pmt = - ir * pv * (pvif + fv) / (pvif - 1);
      if (type === 1)
          pmt /= (1 + ir);
      return pmt;
    },
    renta: function (index) {
      return this.pmt(this.tasa()/12, this.cotizador.plazo, this.total_a_financiar()) * -1
    },
    iva_renta: function (value) {
      return value*.16
    },
    renta_total: function (renta, iva) {
      return renta+iva
    },
    saldo: function (index) {
      var total = this.total_a_financiar()
      var i = 1
      if (this.cotizador.plazo == index){
        return this.renta(null)
      }
      for(i; i < index; i++){
        total = total * this.tasa()/12 - this.renta(null) + total
      }
      return total
    },
  },
  filters: {
    ifnot: function (value) {
      if (!value) return '-'
      return value
    },
    ffecha: function (value) {
      return moment(value).format("DD/MM/YY")
    }
  },
}
</script>
