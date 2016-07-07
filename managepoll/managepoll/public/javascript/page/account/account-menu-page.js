var AccountMenu = function () {

	

	var handleAccountMenu = function () {
		$('a[data-toggle="tab"]').click( function (e) {
			
	    	 
			console.log(e);
			console.log(e.currentTarget.attributes[0].data);
			url = $(e.currentTarget).attr('data');
			console.log(url);
			window.location.href = url;
			 
			
			
		});
		 
	}
    
    return {
        //main function to initiate the module
        init: function () {
        	
             
        	handleAccountMenu();        
	        
        }

    };

}();