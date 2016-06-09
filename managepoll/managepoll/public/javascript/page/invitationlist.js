    $(document).ready(function() {
	
        
        var grid =  $("#grid-data").bootgrid({
            ajax: true,
            post: function ()
            {
                /* To accumulate custom parameter with the request object */
                return {
                    id: $("#id_question_project").val()
                };
            },
            
            url: "/managepoll/getdatainvittation",
            formatters: {
                "commands": function(column, row)
                {
                	//debugger;
                	//console.log(row);
                	return '<button type="button" class="btn btn-primary command-edit" data-row-id="' + row.id_question_project + '" data-row-name="' + row.name +'"><span class="fa fa-pencil"></span></button> ' + 
                    	   '<button type="button" class="btn btn-default command-delete" data-row-id="' + row.id_question_project + '" data-row-name="' + row.name +'"><span class="fa fa-trash-o"></span></button>' +
                    	   '<button type="button" class="btn btn-default command-invitation" data-row-id="' + row.id_question_project + '"><span class="glyphicon glyphicon-envelope"></span></button>' +
             	   		   '<button type="button" class="btn btn-default command-publicationlist" data-row-id="' + row.id_question_project + '"><span class="glyphicon glyphicon-th"></span></button>';

             	   		   
                }
            }
          
        	}).on("loaded.rs.jquery.bootgrid", function(){
        		console.log("loaded.rs.jquery.bootgrid");
            grid.find(".command-edit").on("click", function(e)
            {
            	
               //alert("Edit : " + $(this).data("row-name"));
               window.location.assign("/managepoll/managesurfvey?idproject=" + $(this).data("row-id"))
                
            }).end().find(".command-delete").on("click", function(e)
            {
                alert("Delete ID :" + $(this).data("row-id") + "?");
                window.location.assign("/managepoll/deletesurfvey?idproject=" + $(this).data("row-id"))
               

            }).end().find(".command-invitation").on("click", function(e)
            {
               
                window.location.assign("/managepoll/invitation?idproject=" + $(this).data("row-id"))
                
              	         
            }).end().find(".command-publicationlist").on("click", function(e)
            	    {
            	    	       
            	    	window.location.assign("/managepoll/publicationlist?idproject=" + $(this).data("row-id"))
            	    	         

            });
           
        });
    });	
