var ChangePassword = function () {

	

	var handleChangePassword = function () {

		 
         $('.changepass-form').validate({
	            errorElement: 'span', //default input error message container
	            errorClass: 'help-block', // default input error message class
	            focusInvalid: false, // do not focus the last invalid input
	            ignore: "",
	            rules: {
	                
	            	password: {
		                    required: true
		            }, 
	                 
		            newpassword: {
	                    required: true
	                },
	                rnewpassword: {
	                    equalTo: "#register_newpassword"
	                } 
	            },

	            messages: {  
	            	password: {
	                    required: function() { return window.lang.translate('msg_enter_your_password'); }
		            }, 
	                 
		            newpassword: {
	                    required: function() { return window.lang.translate('enter_new_password'); }
	                },
	                rnewpassword: {
	                    equalTo: function() { return window.lang.translate('retype_password'); }
	                }  
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
	            	
	            	
	            	
	            	/*$.ajax({
	   			     type     : "POST",
	   			     cache    : false,
	   			     url      : '/account/rechangepass',//form.attr('action'),
	   			     data     : $(form).serialize(),//form.serializeArray(),
	   			     success  : function(data) {
	   			    	 console.log('success');
	   			    	 console.log(data);
	   			    	 if(data.success == true){
	   			    		alert("change password success."); 
	   			    		$('.changepass-form')[0].reset();
	   			    		
	   			    		 
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
	   			    });*/
	            	form.submit();
	            }
	        });

			$('.changepass-form input').keypress(function (e) {
	            if (e.which == 13) {
	                if ($('.changepass-form').validate().form()) {
	                    $('.changepass-form').submit();
	                }
	                return false;
	            }
	        });
			
			 
	         
	        
			 
	     
	        //jQuery('.changepass-form').show();
	}
    
    return {
        //main function to initiate the module
        init: function () {
        	
             
        	handleChangePassword();        
        	AccountMenu.init();
            
        }

    };

}();