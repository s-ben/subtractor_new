

var ajaxRequestIntervalMs = 1000;

// var ajaxRequestUrl = './a.txt';
var ajaxRequestUrl = '/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav';
// var ajaxRequestUrl_test = "{{output_url}}";
// console.log("story", ajaxRequestUrl_test, "story");
// {{output_url};

// var loaderImageUrl = './img/ajax-loader.gif';
var loaderImageUrl = '/media/ajax-loader.gif';
var loaderDivName = 'loaderDiv';
 
// http://www.w3schools.com/js/js_obj_boolean.asp
var isLoading=new Boolean(); 
isLoading=false;
 
//JavaScript's built-in setInterval() function
setInterval(
    function(){                      
        $.ajax({
            url: ajaxRequestUrl,
            type: "GET",
            cache: false,                                  
            statusCode: {
                // HTTP-Code "Page not found"
                404: function() {
                    if (isLoading===false){
                        showLoader();
                    }
                },
                // HTTP-Code "Success"
                200: function() {
                    if (isLoading===true){
                        hideLoader();
                    }
                }    
            }
        });     
    },
    ajaxRequestIntervalMs
);
 
// ------------ show- and hide-functions for the overlay -----------------
function showLoader(){
    // $("body").append("<div id='" + loaderDivName + "'><img src='"+loaderImageUrl+"' /></div>");
    var progress_text = $("<p></p>").text("File processing...."); 
    // var progress_text = $("<p></p>").text(ajaxRequestUrl_test); 
    $("#js_test").html(progress_text)
    // $("js_test").html(ajaxRequestUrl_test)
    $("#loaderDiv").append("<div id='" + loaderDivName + "'><img src='"+loaderImageUrl+"' /></div>");
    // $("p").append("<div id='" + loaderDivName + "'><img src='"+loaderImageUrl+"' /></div>");
    isLoading=true;
};
  
function hideLoader(){
    href = '<a href="/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav" target="_blank">Click here to download</a>' ;
    $("#js_test").html(href)
    $("#" + loaderDivName).remove();

    isLoading=false;
};