    $(document).ready(function() {
    	//alert($("#id_question_project").val());
    	
    	 var grid =  $("#grid-data").bootgrid({
    		 	
    		    ajax: true,
    		    post: function ()
    		    {
    		        /* To accumulate custom parameter with the request object */
    		        return {
    		            id: $("#id_question_project").val()
    		        
    		            
    		        };
    		    },
    		    
    		    url: "/managepoll/script/getdatapublication",
    		    
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
    		       window.location.assign("/managepoll/publication/publicationtest?idoption=" + $(this).data("row-id") + "&idproject=" + $("#id_question_project").val())
    		        
    		    }).end().find(".command-delete").on("click", function(e)
    		    {
    		        alert("Delete ID :" + $(this).data("row-id") + "?");
    		        window.location.assign("/managepoll/publication/deletepublication?idoption=" + $(this).data("row-id")+ "&idproject=" + $("#id_question_project").val())
    		 
    		    });
    		});
     
    	 $("#addpublication").click(function(){
    			
    			window.location.assign("/managepoll/publication/publicationtest?idproject=" + $("#id_question_project").val())
    			
    		});

    	 $("#btn_cancel").click(function(){
    			
    			window.location.assign("/managepoll/project")
    			
    		});  
    	 
    });	
    
   
