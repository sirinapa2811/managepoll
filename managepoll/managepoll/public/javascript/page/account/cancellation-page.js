var Cancellation = function () {

	

	var handleCancellation = function () {

		 
         $('#cancellation-form').validate({
	            errorElement: 'span', //default input error message container
	            errorClass: 'help-block', // default input error message class
	            focusInvalid: false, // do not focus the last invalid input
	            ignore: "",
	            rules: {
	               
	            },

	            messages: {  
	            	
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
	            	
	            },

	            submitHandler: function (form) {
	            	
	                $.confirm({
	                    title: window.lang.translate('confirm_deactivate'),
	                    content: window.lang.translate('msg_confirm_deactivate'),
	                    confirmButton : window.lang.translate('yes'),
	                    cancelButton : window.lang.translate('no'),
	                    confirmButtonClass: 'btn-info',
	                    cancelButtonClass: 'btn-danger',
	                    icon: 'fa fa-warning',
	                    closeIcon: true,	                     
	                    confirm: function(){
	                    	form.submit();
	                    }
	                });
	            	
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
	            	//form.submit();
	            }
	        });

			
			 
	         
	        
			 
	     
	      
	}
    
    return {
        //main function to initiate the module
        init: function () {
        	
             
        	handleCancellation();        
        	AccountMenu.init();
        	
        }

    };

}();