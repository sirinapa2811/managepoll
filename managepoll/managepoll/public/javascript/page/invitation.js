    $(document).ready(function() {
	var bodyEditorEN = CKEDITOR.replace( 'content', {toolbar : 'Basic'});
    var body = CKEDITOR.instances['content'];
    	//alert(body);
    	
    var value = CKEDITOR.instances['content'].getData();
    	//console.log(value)
    	
	
    	$("#vol_name").click(function(){
    		var value = body.getData();
    		value = value+"[name]";
    		body.setData(value);
    		
    	});
    	
    	$("#acc_url").click(function(){
    		var value = body.getData();
    		value = value+"<a href='[url]'>[url]</a>";
    		body.setData(value);
    		
    	});
    	
    	$("#init_date").click(function(){
    		var value = body.getData();
    		value = value+"[initialDate]";
    		body.setData(value);
    	});
    	
    	$("#finish_date").click(function(){
    		var value = body.getData();
    		value = value+"[finishDate]";
    		body.setData(value);
    	});
    	
    	$("#save").click(function(){
    		//alert("save");
    		$("#save_inittation").submit();
    		
    	});
    
    	
    	jQuery.validator.setDefaults({
        	debug: true,
        	success: "valid"
        });
        $( "#save_inittation" ).validate({
        	rules: {
        		name_content: {
        			required: true
        		
        		},
        		subject:{
        			required: true
        		},
        		from_name :{
        			required: true
        		}
        		
        	},
            submitHandler: function(form){
            	
            	console.log(form);
            	form.submit();
            }
        });
        
        
      
    });	
