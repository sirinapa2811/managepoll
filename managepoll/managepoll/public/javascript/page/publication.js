    $(document).ready(function() {
    	
	var bodyWelocome = CKEDITOR.replace('welcome_message', {toolbar : 'Basic'});
    var body1 = CKEDITOR.instances['welcome_message'];
    
	var bodyGoodbye = CKEDITOR.replace('end_message', {toolbar : 'Basic'});
	var body2 = CKEDITOR.instances['end_message'];
	
	var bodyHeader = CKEDITOR.replace('header_message', {toolbar : 'Basic'});
	var body3 = CKEDITOR.instances['header_message'];
	
	var bodyFooter = CKEDITOR.replace('footer_message', {toolbar : 'Basic'});
	var body4 = CKEDITOR.instances['footer_message'];
	

    $('#activate_date').datepicker({
    	dateFormat: 'dd/mm/yy',
        minDate: new Date(),
        maxDate: '+1y'
    });

    $('#expire_date').datepicker({
    	dateFormat: 'dd/mm/yy',
        startDate: '18/05/2016'
    });
    
    
    
  
    
    jQuery.validator.setDefaults({
    	debug: true,
    	success: "valid"
    });
    $( "#save_publication" ).validate({
    	rules: {
    		name_publication: {
    			required: true
    		
    		},
    		use_question_no : {
    			required: true
    		},
    		duration_time  : {
    			required: true
    		},
    		activate_date : {
    			required: true
    		},
    		expire_date: {
    			required: true
    		},
    		redirect_url: {
    			required: true
    		},
    		id_question_theme: {
    		      required: true
    		    },
    		id_close_type: {
    		      required: true
    	    },
    		id_question_invitation: {
    		      required: true
    	    },
    		id_fix_random_type: {
    		      required: true
    	    }
    	    
    	},
    submitHandler: function(form){
    	
    	console.log(form);
    	form.submit();
    }
    });

    $("#btn_cancel").click(function(){
		
		window.location.assign("/managepoll/publicationlist?idproject=" + $("#id_question_project").val())
		
	});
 

    
    });
    	
