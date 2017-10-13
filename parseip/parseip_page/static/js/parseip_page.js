// When user clicks button, grab input
// Run that input through python method
// Display the results back on the page


var handleClick = function() {
  var input = $( 'input' );
  var request = $.post(url="/ajax/parseip_page/", format="json", data=input);
  request.done(function(data) {
    $( '<textarea id="returnedParse">data</textarea>' );
  });
}

$( 'button' ).on('click', handleClick);
