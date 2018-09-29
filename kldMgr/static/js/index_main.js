alert("hellow, world!")


$(document).ready(function(){

    $("image").on("click", function(e){
        gele = $(e.target).parent()
        alert($(gele).attr("id"))
    })

})

