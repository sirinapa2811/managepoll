$(document).ready(function() {	
    	
    $('#birthdate').datepicker({
    	dateFormat: 'yy-mm-dd',
        startDate: '18/05/2016'
    });
    
    $("#id_employment_status_type").change(function () {
        var selectedText = $(this).find("option:selected").text();
        var selectedValue = $(this).val();         
        
        if ($(this).val() == ""){        	
        	$("#intructry_type").hide();
            $("#job_catagory").hide();
        }
        if ($(this).val() == "1"){
        	//alert("Selected Text: " + selectedText + " Value: " + selectedValue);    
        	$("#intructry_type").show();
            $("#job_catagory").show();
        }
        if ($(this).val() == "2"){
        	//alert("Selected Text: " + selectedText + " Value: " + selectedValue);  
        	$("#intructry_type").show();
            $("#job_catagory").show();
        }
        if ($(this).val() == "3"){
        	//alert("Selected Text: " + selectedText + " Value: " + selectedValue); 
        	$("#intructry_type").hide();
            $("#job_catagory").hide();
        }
    });
  

	
/*    debugger*/
    
	$("#select_country").select2({
	  	placeholder: '<i class="fa fa-map-marker"></i>&nbsp;Select a Country',
        allowClear: true,
       // formatResult: format,
        //formatSelection: format,
        escapeMarkup: function (m) {
            return m;
        }
    });

	
	$("#frm_voter").validate();
	
	$("#btn_cancel").click(function(){
		
		window.location.assign("/managepoll/voter")
		
	});
	
    });

