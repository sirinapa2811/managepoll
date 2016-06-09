    $(document).ready(function() {
    	//alert($("#idproject").val());
    	 var grid =  $("#grid-data").bootgrid({
    		 	
    		    ajax: true,
    		    post: function ()
    		    {
    		        /* To accumulate custom parameter with the request object */
    		        return {
    		            id: $("#idproject").val()
    		        
    		            
    		        };
    		    },
    		    url: "/getdatapublication",
    		    
    		    formatters: {
    		        "commands": function(column, row)
    		        {
    		        	//debugger;
    		        	//console.log(row);
    		        	return '<button type="button"  class="btn btn-primary command-edit" data-row-id="' + row.id_question_option + '" data-row-name="' + row.name +'"><span class="fa fa-pencil"></span></button> ' + 
    		            	   '<button type="button" class="btn btn-default command-delete" data-row-id="' + row.id_question_option + '"><span class="fa fa-trash-o"></span></button>' ;
    		            
    		     	   		   
    		        }
    		    }
    		  
    			}).on("loaded.rs.jquery.bootgrid", function(){
    				console.log("loaded.rs.jquery.bootgrid");
    		    grid.find(".command-edit").on("click", function(e)
    		    {
    		    	
    		      // alert("Edit : " + $(this).data("row-id"));
    		       window.location.assign("/publication?idoption=" + $(this).data("row-id") + "&idproject=" + $("#idproject").val())
    		        
    		    }).end().find(".command-delete").on("click", function(e)
    		    {
    		        alert("Delete ID :" + $(this).data("row-id") + "?");
    		        window.location.assign("/deletepublication?idoption=" + $(this).data("row-id")+ "&idproject=" + $("#idproject").val())
    		       

    		         

    		    });
    			 });
     
    	 $("#addpublication").click(function(){
    			
    			window.location.assign("/publication?idproject=" + $("#idproject").val())
    			
    		});

    	 $("#btn_cancel").click(function(){
    			
    			window.location.assign("/surfvey")
    			
    		});  
    	 
    });	
    
   
