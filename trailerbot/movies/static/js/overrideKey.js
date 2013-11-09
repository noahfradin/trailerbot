$(function() {
  $(document).keyup(function(evt) {
    if (evt.keyCode == 32) {
      console.log("space bar not pressed"); 
    }
  }).keydown(function(evt) {
    if (evt.keyCode == 37) {
      console.log("left arrow is pressed"); 
    }
    else if(evt.keyCode == 39){
        console.log("right arrow is pressed"); 
    }
    // Konami code??!?!?!?!?
  });
}); 