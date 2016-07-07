var Account = function () {
 

	var handleAccount = function () {
		
		if (jQuery().datepicker) {
            $('.date-picker').datepicker({
               // rtl: Metronic.isRTL(),
            	todayHighlight: true,
                autoclose: true,
                language: "th"
            });
            //$('body').removeClass("modal-open"); // fix bug when inline picker is used in modal
        }
		
		function format(state) {
			
            if (!state.id) return state.text; // optgroup
            return "<img class='flag' src='/theme/assets/global/img/flags/" + state.id.toLowerCase() + ".png'/>&nbsp;&nbsp;" + state.text;
        }
		$("#select2_sample4").select2({
		  	placeholder: '<i class="fa fa-map-marker"></i>&nbsp;Select a Country',
            allowClear: true,
            formatResult: format,
            formatSelection: format,
            escapeMarkup: function (m) {
                return m;
            }
        });
		$('#select2_sample4').change(function () {
            $('.accountsetting-form').validate().element($(this)); //revalidate the chosen dropdown value and show error or success message for the input
        });
		
		
		function formatGender(state) {
            if (!state.id) return state.text; // optgroup
            return "<img class='flag' src='/img/survey/register-gender/" + state.id.toLowerCase() + ".png'/>&nbsp;&nbsp;" + state.text;
        }
		$("#select2_sample5").select2({
		  	placeholder: '<i class="fa fa-user"></i>&nbsp;Select a Gender',
            allowClear: true,
            formatResult: formatGender,
            formatSelection: formatGender,
            escapeMarkup: function (m) {
                return m;
            }
        });
		$('#select2_sample5').change(function () {
            $('.accountsetting-form').validate().element($(this)); //revalidate the chosen dropdown value and show error or success message for the input
        });
		
		
		//////////////
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
		$('#select_language').change(function () {
            $('.accountsetting-form').validate().element($(this)); //revalidate the chosen dropdown value and show error or success message for the input
        });
		
		/////////////
		
		
		
		 $('.accountsetting-form').validate({
	            errorElement: 'span', //default input error message container
	            errorClass: 'help-block', // default input error message class
	            focusInvalid: false, // do not focus the last invalid input
	            ignore: "",
	            rules: {  },

	            messages: {
	            	
	            	first_name :{required: function() { return window.lang.translate('msg_enter_your_name'); }  },
	            	last_name :{required: function() { return window.lang.translate('msg_enter_your_lastname'); }  },
	            	id_gender :{required: function() { return window.lang.translate('msg_enter_your_gender'); }  },
	            	birthdate :{required: function() { return window.lang.translate('msg_enter_birthdate'); }  },
	            	address :{required: function() { return window.lang.translate('msg_enter_your_address'); }  },
	            	city :{required: function() { return window.lang.translate('msg_enter_your_city'); }  },
	            	post_code :{required: function() { return window.lang.translate('msg_enter_your_post_code'); }  },
	            	country :{required: function() { return window.lang.translate('msg_enter_your_country'); }  },
	            	language :{required: function() { return window.lang.translate('msg_enter_your_language'); }  }
	            	 
	            },

	            invalidHandler: function (event, validator) { //display error alert on form submit   

	            },

	            highlight: function (element) { // hightlight error inputs
	                $(element)
	                    .closest('.form-group').addClass('has-error'); // set error class to the control group
	            },

	            success: function (label) {
	                label.closest('.form-group').removeClass('has-error');
	                label.remove();
	            },

	            errorPlacement: function (error, element) {
	            	if (element.attr("name") == "tnc") { // insert checkbox errors after the container                  
	                    error.insertAfter($('#register_tnc_error'));
	                } else if (element.closest('.input-icon').size() === 1) {
	                    error.insertAfter(element.closest('.input-icon'));
	                } else {
	                	error.insertAfter(element);
	                }
	            },

	            submitHandler: function (form) {
	            	  
	            	$.ajax({
	   			     type     : "POST",
	   			     cache    : false,
	   			     url      : '/account/updateprofile',//form.attr('action'), ofile')}
	   			     data     : $(form).serialize(),//form.serializeArray(),
	   			     success  : function(data) {
	   			    	 console.log('success');
	   			    	 
	   			    	 if(data.success == true){
	   			    		alert("change password success."); 
	   			    		//$('.changepass-form')[0].reset();
	   			    		
	   			    		 
	   			    		// $(location).attr('href',"/register/registerSuccess"); 
	   			    	 }
	   			    	 else {
	   			    		alert(data.message);
	   			    		//$('.changepass-form')[0][2].value='';
	   			    		 return false;
	   			    	 }
	   			     },
	   			    error: function (responseData) {
	   			    	console.log(responseData);
	   			    	alert("server not response. please try again");
	                    console.log('Ajax request not recieved!');
	                }
	   			    });
	            	//form.submit();
	            }
	        });
			

		 
	}
    
    return {
        //main function to initiate the module
        init: function () {
        	
             
        	handleAccount();      
        	
        	//handleDatePickers();
            //handleTimePickers();
            //handleDatetimePicker();
            //handleDateRangePickers();
            //handleClockfaceTimePickers();
            //handleColorPicker();
            
        	
        	AccountMenu.init();
        }

    };

}();