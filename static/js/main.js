// A $( document ).ready() block.
$( document ).ready(function() {

	// $("#js_test").hide(300).show(1000);

	// $.get("/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav")
 //    	.done(function() { 
 //    		$("#js_test").html('file exists!')
 //        // exists code 
        
 //    	}).fail(function() { 
 //    		$("#js_test").html('nope')
 //        // not exists code
 //   		 })

	
	$.ajax({
	    url:'/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav',
	    type:'HEAD',
	    error: function()
	    {
	    	// WORKING CODE BELOW....
	    	// var txt2 = $("<p></p>").text("FILE PROCESSING....."); 
	    	// $("#js_test").html(txt2)
	    	var ajaxRequestUrl_test = {{output_url}};
	    	$("#js_test").html(ajaxRequestUrl_test)


	    	// href = '<a href="http://127.0.0.1:8000/audio_process/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav">Output file TEST</a>' ;
	    	// href = '<a href="/audio_process/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav">Output file TEST</a>' ;
	    	// $("#js_test").html(txt2)
	    	
	    	// $("#js_test").html('file does not exist')
	        //file does not exist
	    },
	    success: function()
	    {

	    		    	// WORKING CODE BELOW.....

	    	href = '<a href="/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav">Output file TEST</a>' ;
	    	// href = '<a href="http://127.0.0.1:8000/audio_process/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav">Output file TEST</a>' ;
	    		
	    	var txt2 = $("<p></p>").text("FILE Present...."); 
	    	$("#js_test").html(href)
	    	var ajaxRequestUrl_test = {{output_url}};
	    	$("#js_test").html(ajaxRequestUrl_test)

	    	
	    	// $('<a href="/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav">Output file</a>');  
	    	// var link = '<a href="/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav">Output file</a>'
	    	// href = '<a href="http://127.0.0.1:8000/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav">Output file TEST</a>' ;
	    	





	    	// $("#js_test").html(href)

	    	// var txt2 = $("<p></p>").text("Text."); 
	    	// <a href="/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav">Output file</a>
	    	// $("#js_test").append(link)
	    	// $("#js_test").html(txt2)
	        //file exists do something here
	    }
	});

	// $.get( "/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav", function( r, text_status ) {

	// $("#js_test").html('file exists!')
	// console.log(text_status);
	// console.log('testing');
 //    response = r;
	// });


	// $.ajax({ cache: false,
	//   url: "/Admin/Contents/GetData",
	//   data: { accountID: AccountID },
	//   success: function (data) {
	//   $('#CityID').html(data);
	//   },
	//   error: function (ajaxContext) {
	//   alert(ajaxContext.responseText)
	//   }
	// });

    // console.log( "ready!" );
});

