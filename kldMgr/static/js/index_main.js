alert("hellow, world!")


$(document).ready(function(){

    $("image").on("click", function(e){
        gele = $(e.target).parent().parent()
        gele = $(gele).children("g.comment")
        gele.toggle()
    })

})

