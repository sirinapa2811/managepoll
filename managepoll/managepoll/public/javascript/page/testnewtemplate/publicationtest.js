    $(document).ready(function() {
    	
	var bodyWelocome = CKEDITOR.replace('welcome_message', {toolbar : 'Basic'});
    var body1 = CKEDITOR.instances['welcome_message'];
    
	var bodyGoodbye = CKEDITOR.replace('end_message', {toolbar : 'Basic'});
	var body2 = CKEDITOR.instances['end_message'];
	
	var bodyHeader = CKEDITOR.replace('header_message', {toolbar : 'Basic'});
	var body3 = CKEDITOR.instances['header_message'];
	
	var bodyFooter = CKEDITOR.replace('footer_message', {toolbar : 'Basic'});
	var body4 = CKEDITOR.instances['footer_message'];
	
	if (jQuery().datepicker) {
		$('#activate_date').datepicker({
			dateFormat: 'dd/mm/yy',
			todayHighlight: true,
	        autoclose: true,
	        language: "th"
	    });

	    $('#expire_date').datepicker({
	    	dateFormat: 'dd/mm/yy',
	    	todayHighlight: true,
	        autoclose: true,
	        language: "th"
	    });
    };
	


    /*$('#activate_date').datepicker({
    	dateFormat: 'dd/mm/yy',
        minDate: new Date(),
        maxDate: '+1y'
    });

    $('#expire_date').datepicker({
    	dateFormat: 'dd/mm/yy',
        startDate: '18/05/2016'
    });*/
    
    

    //debugger;
    
   $("#id_question_invitation").select2({	  	
    	placeholder: 'Select E-mail Template',
        allowClear: true,       
        escapeMarkup: function (m) {
            return m;
        }
    });
    
    $("#add_invitation").click(function(){
   
    	$.confirm({ 
            title: window.lang.translate('confirm_invitation'), 
            content: window.lang.translate('msg_confirm_invitation'), 
            confirmButton : window.lang.translate('yes'), 
            cancelButton : window.lang.translate('no'), 
            confirmButtonClass: 'btn-info', 
            cancelButtonClass: 'btn-danger', 
            icon: 'fa fa-warning', 
            closeIcon: true,                       
            confirm: function(){
            	 window.location.assign("/managepoll/invitation/invitationtest")
            }
    	
    	})
    });
    
	
 
    
    $("#save_publication" ).validate();

    $("#btn_cancel").click(function(){
		
		window.location.assign("/managepoll/publication/indextest?idproject=" + $("#id_question_project").val())
		
	});

    });
    function resetfield() {	
    	
		document.getElementById("save_publication").reset();
	}
    	
