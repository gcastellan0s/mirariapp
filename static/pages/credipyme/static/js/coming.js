$(document).ready(function(){$("#ms-countdown").countdown("2017/09/07",function(l){$(this).html(l.strftime('<ul class="coming-date coming-date-black"><li>%D <span>Days</span></li><li class="colon">:</li><li>%H <span>Hours</span></li><li class="colon">:</li><li>%M <span>Minutes</span></li><li class="colon">:</li><li>%S <span>Seconds</span></li></ul>'))})});