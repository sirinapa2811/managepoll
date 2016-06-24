    $(document).ready(function() {
    	//alert($("#id_question_project").val());
        
        var grid =  $("#grid-data").bootgrid({
            ajax: true,
            post: function ()
            {
                /* To accumulate custom parameter with the request object */
                return {
                	id: "b0df282a-0d67-40e5-8558-c9e93b7befed"
                
                };
            },
        
            url: "/managepoll/script/getdatainvittation",
            
            
            formatters: {
		        "commands": function(column, row)
		        {
		        	//debugger;
		        	//console.log(row);
		        	return '<button type="button"  class="btn btn-primary command-edit" data-row-id="' + row.id_question_invitation + '" data-row-name="' + row.name +'"><span class="fa fa-pencil"></span></button> ' + 
		            	   '<button type="button" class="btn btn-default command-delete" data-row-id="' + row.id_question_invitation + '"><span class="fa fa-trash-o"></span></button>' ;
		            
		     	   		   
		        }
		    }
        }).on("loaded.rs.jquery.bootgrid", function(){
			console.log("loaded.rs.jquery.bootgrid");
	    grid.find(".command-edit").on("click", function(e)
	    {
	    	
	      // alert("Edit : " + $(this).data("row-id"));
	       window.location.assign("/managepoll/invitation/invitation?idinvitation=" + $(this).data("row-id"))
	        
	    }).end().find(".command-delete").on("click", function(e)
	    {
	        alert("Delete ID :" + $(this).data("row-id") + "?");
	        window.location.assign("/managepoll/invitation/deleteinvitation?idinvitation=" + $(this).data("row-id"))
	
	    });
	});
		
        
        $("#addinvitation").click(function(){
			
			window.location.assign("/managepoll/invitation/invitation")
			
		});

	 
	 
    });	