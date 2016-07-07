$(document).ready(function() {	
	
	 $('#birthdate').datepicker({
	    	dateFormat: 'yy-mm-dd',
	        startDate: '18/05/2016'
	    });
	
	 function formatGender(state) {
         if (!state.id) return state.text; // optgroup
         return "<img class='flag' src='/img/survey/register-gender/" + state.id.toLowerCase() + ".png'/>&nbsp;&nbsp;" + state.text;
     }
		$("#id_gender").select2({	
			placeholder: '<i class="fa fa-user"></i>&nbsp;Select a Gender',
	        allowClear: true,      	    
	        formatResult: formatGender,
            formatSelection: formatGender,
	        escapeMarkup: function (m) {
	            return m;
	        }
	    });
		
		function formatLanguage(state) {
            if (!state.id) return state.text; // optgroup
            return "<img class='flag' src='/theme/assets/global/img/flags/" + state.id.toLowerCase() + ".png'/>&nbsp;&nbsp;" + state.text;
			
			
        }
		$("#select_language").select2({
		  	placeholder: '<i class="fa fa-map-marker"></i>&nbsp;Select Language',
            allowClear: true,
            formatResult: formatLanguage,
            formatSelection: formatLanguage,
            escapeMarkup: function (m) {
                return m;
            }
        });
		
		
function format(state) {
			
            if (!state.id) return state.text; // optgroup
            return "<img class='flag' src='/theme/assets/global/img/flags/" + state.id.toLowerCase() + ".png'/>&nbsp;&nbsp;" + state.text;
        }
		$("#select_country").select2({
		  	placeholder: '<i class="fa fa-map-marker"></i>&nbsp;Select a Country',
            allowClear: true,
            formatResult: format,
            formatSelection: format,
            escapeMarkup: function (m) {
                return m;
            }
        });
		
	
});

    	
   