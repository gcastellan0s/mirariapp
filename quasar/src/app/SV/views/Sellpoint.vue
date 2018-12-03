<template>
  <div class="row">
    <div class="col-sm-12 col-xl-4">
        <div class="card mb-4">
            <h6 class="card-header with-elements border-0 pr-0 pb-0">
                <div class="card-header-title">Sales</div>
                <div class="card-header-elements ml-auto">
                    <div id="__BVID__353" class="dropdown-toggle-hide-arrow mr-3 btn-group b-dropdown dropdown">
                        <!---->
                        <button id="__BVID__353__BV_toggle_" aria-haspopup="true" aria-expanded="false" type="button" class="btn btn-default icon-btn borderless btn-round md-btn-flat btn-sm dropdown-toggle">
                            <i class="ion ion-ios-more"></i>
                        </button>
                        <div role="menu" aria-labelledby="__BVID__353__BV_toggle_" class="dropdown-menu dropdown-menu-right">
                            <a role="menuitem" href="#" target="_self" class="dropdown-item">Action 1</a>
                            <a role="menuitem" href="#" target="_self" class="dropdown-item">Action 2</a>
                        </div>
                    </div>
                </div>
            </h6>
            <div class="mt-3">
                <div class="">
                    <canvas id="line-chart" width="878" height="200" style="display: block; height: 100px; width: 439px;"></canvas>
                </div>
            </div>
            <div class="card-footer text-center py-2">
                <div class="row">
                    <div class="col">
                        <div class="text-muted small">Target</div>
                        <strong class="text-big">500</strong>
                    </div>
                    <div class="col">
                        <div class="text-muted small">Current</div>
                        <strong class="text-big">421</strong>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-xl-4">
        <div class="card mb-4">
            <div class="card-body">
                <div class="float-right text-success">
                    <small class="ion ion-md-arrow-round-up text-tiny"></small> 12%
                </div>
                <div class="text-muted small">Total revenue</div>
                <div class="text-xlarge">$1,534</div>
            </div>
            <div class="px-2">
                <div class="w-100">
                    <canvas id="bar-chart" width="846" height="234" style="display: block; height: 117px; width: 423px;"></canvas>
                </div>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-xl-4">
        <div class="card mb-4">
            <div class="card-body pb-0">
                <div class="text-right small mb-4">Aug 2017 - Feb 2018</div>
                <div class="my-3">
                    <canvas id="line-chart" width="782" height="172" style="display: block; height: 86px; width: 391px;"></canvas>
                </div>
            </div>
            <div class="card-footer">
                <button type="button" class="btn btn-xs icon-btn float-right btn-outline-primary">
                    <i class="ion ion-md-sync"></i>
                </button>
                Unique visitors
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-xl-3">
        <div class="card mb-4">
            <h6 class="card-header bg-success text-white">
                <i class="ion ion-md-cash"></i>&nbsp; Revenue
            </h6>
            <div class="bg-success text-white">
                <div class="d-flex align-items-center position-relative mt-4" style="height: 140px;">
                    <div class="w-100 position-absolute" style="top: 0px;">
                        <canvas id="doughnut-chart" width="648" height="280" style="display: block; height: 140px; width: 324px;"></canvas>
                    </div>
                    <div class="w-100 text-center text-xlarge">85</div>
                </div>
                <div class="text-center mt-3 mb-4">
                    Sales today
                </div>
            </div>
            <div class="card-footer border-0 text-center py-3">
                <div class="row">
                    <div class="col">
                        <div class="text-muted small mb-1">Target</div>
                        <strong class="text-big">$1225</strong>
                    </div>
                    <div class="col">
                        <div class="text-muted small mb-1">Current</div>
                        <strong class="text-big">$654</strong>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xl-9">
        <div class="row">
            <div class="col-md-6">
                <div class="card mb-4">
                    <h6 class="card-header with-elements">
                        <div class="card-header-title">Tasks</div>
                        <div class="card-header-elements ml-auto">
                            <button type="button" class="btn btn-xs md-btn-flat btn-default">Show more</button>
                        </div>
                    </h6>
                    <div class="ps ps--active-y" style="height: 234px;">
                        <div class="card-body">
                            <p class="text-muted small">Today</p>
                            <div class="custom-controls-stacked">
                                <div class="ui-todo-item custom-control custom-checkbox custom-control-inline">
                                    <input id="__BVID__359" type="checkbox" autocomplete="off" true-value="true" class="custom-control-input"
                                        value="true">
                                    <label for="__BVID__359" class="custom-control-label">
                                        Buy products
                                        <span class="ui-todo-badge badge badge-outline-default font-weight-normal ml-2">58 mins left</span>
                                    </label>
                                </div>
                                <div class="ui-todo-item custom-control custom-checkbox custom-control-inline">
                                    <input id="__BVID__360" type="checkbox" autocomplete="off" true-value="true" class="custom-control-input"
                                        value="true">
                                    <label for="__BVID__360" class="custom-control-label">Reply to emails</label>
                                </div>
                                <div class="ui-todo-item custom-control custom-checkbox custom-control-inline">
                                    <input id="__BVID__361" type="checkbox" autocomplete="off" true-value="true" class="custom-control-input"
                                        value="true">
                                    <label for="__BVID__361" class="custom-control-label">
                                        Write blog post
                                        <span class="ui-todo-badge badge badge-outline-default font-weight-normal ml-2">20 hours left</span>
                                    </label>
                                </div>
                                <div class="ui-todo-item custom-control custom-checkbox custom-control-inline">
                                    <input id="__BVID__362" type="checkbox" autocomplete="off" true-value="true" class="custom-control-input"
                                        value="true">
                                    <label for="__BVID__362" class="custom-control-label">Wash my car</label>
                                </div>
                            </div>
                        </div>
                        <hr class="m-0">
                        <div class="card-body">
                            <p class="text-muted small">Tomorrow</p>
                            <div class="custom-controls-stacked">
                                <div class="ui-todo-item custom-control custom-checkbox custom-control-inline">
                                    <input id="__BVID__363" type="checkbox" autocomplete="off" true-value="true" class="custom-control-input"
                                        value="true">
                                    <label for="__BVID__363" class="custom-control-label">Buy antivirus</label>
                                </div>
                                <div class="ui-todo-item custom-control custom-checkbox custom-control-inline">
                                    <input id="__BVID__364" type="checkbox" autocomplete="off" true-value="true" class="custom-control-input"
                                        value="true">
                                    <label for="__BVID__364" class="custom-control-label">Jane's Happy Birthday</label>
                                </div>
                                <div class="ui-todo-item custom-control custom-checkbox custom-control-inline">
                                    <input id="__BVID__365" type="checkbox" autocomplete="off" true-value="true" class="custom-control-input"
                                        value="true">
                                    <label for="__BVID__365" class="custom-control-label">Call mom</label>
                                </div>
                            </div>
                        </div>
                        <div class="ps__rail-x" style="left: 0px; bottom: 0px;">
                            <div class="ps__thumb-x" tabindex="0" style="left: 0px; width: 0px;"></div>
                        </div>
                        <div class="ps__rail-y" style="top: 0px; height: 234px; right: 0px;">
                            <div class="ps__thumb-y" tabindex="0" style="top: 0px; height: 149px;"></div>
                        </div>
                    </div>
                    <div class="card-footer">
                        <div role="group" class="input-group">
                            <input id="__BVID__366" type="text" placeholder="Type your task" class="form-control">
                            <div class="input-group-append">
                                <button type="button" class="btn btn-primary">Add</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card mb-4">
                    <h6 class="card-header with-elements">
                        <div class="card-header-title">Team TODO</div>
                        <div class="card-header-elements ml-auto">
                            <button type="button" class="btn btn-xs md-btn-flat btn-default">Show more</button>
                        </div>
                    </h6>
                    <div class="ps ps--active-y" style="height: 300px;">
                        <div class="card-body">
                            <div class="rounded ui-bordered p-3 mb-3">
                                Lorem ipsum dolor sit amet, vis erat denique in, dicunt prodesset te vix.
                                <div class="media align-items-center mt-3">
                                    <img src="/products/appwork/v110/assets_/img/avatars/12-small.png" alt="" class="d-block ui-w-30 rounded-circle">
                                    <div class="media-body ml-2">Arthur Duncan</div>
                                    <div class="text-muted small text-nowrap">02/08/2018</div>
                                </div>
                            </div>
                            <div class="rounded ui-bordered p-3 mb-3">
                                Sit meis deleniti eu, pri vidit meliore docendi ut.
                                <div class="media align-items-center mt-3">
                                    <img src="/products/appwork/v110/assets_/img/avatars/11-small.png" alt="" class="d-block ui-w-30 rounded-circle">
                                    <div class="media-body ml-2">Belle Ross</div>
                                    <div class="text-muted small text-nowrap">02/06/2018</div>
                                </div>
                            </div>
                            <div class="rounded ui-bordered p-3">
                                Cum ea graeci tractatos.
                                <div class="media align-items-center mt-3">
                                    <img src="/products/appwork/v110/assets_/img/avatars/10-small.png" alt="" class="d-block ui-w-30 rounded-circle">
                                    <div class="media-body ml-2">Wayne Morgan</div>
                                    <div class="text-muted small text-nowrap">02/04/2018</div>
                                </div>
                            </div>
                        </div>
                        <div class="ps__rail-x" style="left: 0px; bottom: 0px;">
                            <div class="ps__thumb-x" tabindex="0" style="left: 0px; width: 0px;"></div>
                        </div>
                        <div class="ps__rail-y" style="top: 0px; height: 300px; right: 0px;">
                            <div class="ps__thumb-y" tabindex="0" style="top: 0px; height: 238px;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-8">
        <div class="card mb-4">
            <h6 class="card-header with-elements">
                <div class="card-header-title">Sale stats</div>
                <div class="card-header-elements ml-auto">
                    <button type="button" class="btn btn-xs md-btn-flat btn-default">Show more</button>
                </div>
            </h6>
            <div class="table-responsive">
                <table class="table card-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Sales</th>
                            <th>Cancelled</th>
                            <th>Delivered</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>02/08/2018</td>
                            <td>12</td>
                            <td>1</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>02/07/2018</td>
                            <td>16</td>
                            <td>2</td>
                            <td>8</td>
                        </tr>
                        <tr>
                            <td>02/06/2018</td>
                            <td>5</td>
                            <td>0</td>
                            <td>2</td>
                        </tr>
                        <tr>
                            <td>02/05/2018</td>
                            <td>21</td>
                            <td>1</td>
                            <td>10</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card mb-4">
            <h6 class="card-header with-elements">
                <div class="card-header-title">Type gadgets</div>
                <div class="card-header-elements ml-auto">
                    <button type="button" class="btn btn-xs icon-btn md-btn-flat btn-outline-primary">
                        <i class="ion ion-md-sync"></i>
                    </button>
                </div>
            </h6>
            <div class="py-4 px-3">
                <div class="">
                    <canvas id="pie-chart" width="814" height="324" style="display: block; height: 162px; width: 407px;"></canvas>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-6 col-lg-12 col-xl-6">
        <div class="card mb-4">
            <h6 class="card-header">Comments</h6>
            <div class="card-body">
                <div class="media pb-1 mb-3">
                    <img src="/products/appwork/v110/assets_/img/avatars/9-small.png" alt="" class="d-block ui-w-40 rounded-circle">
                    <div class="media-body ml-3">
                        <a href="javascript:void(0)">Amanda Warner</a>
                        <span class="text-muted">commented on</span>
                        <a href="javascript:void(0)">Article Name</a>
                        <p class="my-1">Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo.</p>
                        <div class="clearfix">
                            <a href="javascript:void(0)" class="float-right text-lightest small">
                                <span class="ion ion-ios-thumbs-down"></span>
                            </a>
                            <a href="javascript:void(0)" class="float-right text-lightest small">
                                <span class="ion ion-ios-thumbs-up mr-2"></span>
                            </a>
                            <span class="float-left text-muted small">2 hours ago</span>
                        </div>
                    </div>
                </div>
                <div class="media pb-1 mb-3">
                    <img src="/products/appwork/v110/assets_/img/avatars/8-small.png" alt="" class="d-block ui-w-40 rounded-circle">
                    <div class="media-body ml-3">
                        <a href="javascript:void(0)">Hallie Lewis</a>
                        <span class="text-muted">commented on</span>
                        <a href="javascript:void(0)">Article Name</a>
                        <p class="my-1">Vivendum torquatos ut nec, sit audiam deterruisset ei, cu sed nibh autem scriptorem. Ea quo vidit
                            deleniti constituto, ex qui malis mollis iudicabit, viris fabellas id has.</p>
                        <div class="clearfix">
                            <a href="javascript:void(0)" class="float-right text-lightest small">
                                <span class="ion ion-ios-thumbs-down"></span>
                            </a>
                            <a href="javascript:void(0)" class="float-right text-lightest small">
                                <span class="ion ion-ios-thumbs-up mr-2"></span>
                            </a>
                            <span class="float-left text-muted small">2 hours ago</span>
                        </div>
                    </div>
                </div>
                <div class="media">
                    <img src="/products/appwork/v110/assets_/img/avatars/7-small.png" alt="" class="d-block ui-w-40 rounded-circle">
                    <div class="media-body ml-3">
                        <a href="javascript:void(0)">Alice Hampton</a>
                        <span class="text-muted">commented on</span>
                        <a href="javascript:void(0)">Article Name</a>
                        <p class="my-1">Eam facilis laboramus reprehendunt ei, ex esse fastidii per.</p>
                        <div class="clearfix">
                            <a href="javascript:void(0)" class="float-right text-lightest small">
                                <span class="ion ion-ios-thumbs-down"></span>
                            </a>
                            <a href="javascript:void(0)" class="float-right text-lightest small">
                                <span class="ion ion-ios-thumbs-up mr-2"></span>
                            </a>
                            <span class="float-left text-muted small">2 hours ago</span>
                        </div>
                    </div>
                </div>
            </div>
            <a href="javascript:void(0)" class="card-footer d-block text-center text-dark small font-weight-semibold">SHOW MORE</a>
        </div>
    </div>
    <div class="col-md-6 col-lg-12 col-xl-6">
        <div class="card mb-4">
            <h6 class="card-header">Support tickets</h6>
            <div class="card-body">
                <div class="pb-1 mb-3">
                    <div class="badge badge-outline-warning float-right">Feature</div>
                    <a href="javascript:void(0)">Lorem ipsum dolor sit amet, vis erat denique in.</a>&nbsp;
                    <span class="text-muted">#34563</span>
                    <br>
                    <small class="text-muted">Created by
                        <a href="javascript:void(0)" class="text-dark">Mike Greene</a> &nbsp;·&nbsp; 1 day ago</small>
                </div>
                <div class="pb-1 mb-3">
                    <div class="badge badge-outline-danger float-right">Bug</div>
                    <a href="javascript:void(0)">Dicunt prodesset te vix.</a>&nbsp;
                    <span class="text-muted">#34524</span>
                    <br>
                    <small class="text-muted">Created by
                        <a href="javascript:void(0)" class="text-dark">Leon Wilson</a> &nbsp;·&nbsp; 1 day ago</small>
                </div>
                <div class="pb-1 mb-3">
                    <div class="badge badge-outline-success float-right">Question</div>
                    <a href="javascript:void(0)">Sit meis deleniti eu, pri vidit meliore docendi ut?</a>&nbsp;
                    <span class="text-muted">#34563</span>
                    <br>
                    <small class="text-muted">Created by
                        <a href="javascript:void(0)" class="text-dark">Allie Rodriguez</a> &nbsp;·&nbsp; 1 day ago</small>
                </div>
                <div class="pb-1 mb-3">
                    <div class="badge badge-outline-secondary float-right">Enhancement</div>
                    <a href="javascript:void(0)">Eu tantas offendit mnesarchum sit, vide novum ad pri.</a>&nbsp;
                    <span class="text-muted">#34563</span>
                    <br>
                    <small class="text-muted">Created by
                        <a href="javascript:void(0)" class="text-dark"> Kenneth Frazier</a> &nbsp;·&nbsp; 1 day ago</small>
                </div>
                <div>
                    <div class="badge badge-outline-danger float-right">Bug</div>
                    <a href="javascript:void(0)">Dicunt prodesset te vix.</a>&nbsp;
                    <span class="text-muted">#34524</span>
                    <br>
                    <small class="text-muted">Created by
                        <a href="javascript:void(0)" class="text-dark">Leon Wilson</a> &nbsp;·&nbsp; 1 day ago</small>
                </div>
            </div>
            <a href="javascript:void(0)" class="card-footer d-block text-center text-dark small font-weight-semibold">SHOW MORE</a>
        </div>
    </div>
  </div>
</template>
<script>
  import moment from 'moment'
  export default {
    name: 'forms-extras',
    metaInfo: {
        title: require('@/../../package.json').title,
        titleTemplate: '%s :: ' + require('@/../../package.json').slogan
    },
    data: () => ({
      hoy: moment().format("DD/MM/YY"),
    }),
    mounted: function () {
      this.$store.dispatch('SV/set_sellpoint',)
    }, 
  }
</script>
