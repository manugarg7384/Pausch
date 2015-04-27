$(function() {
  init();

  $('.wrap button').click(function()  {
    console.log(this.innerHTML);
    var data = {
      index: 22 - this.innerHTML
    }
    $.ajax({
        url: '/change-panel',
        method: 'GET',
        data: data,
        dataType: 'html',
        success: success
    });

    function success(data) {
      console.log(data);
      document.write(data);
    }
  });
});

function init() {
  //open popup
  $('.cd-popup-trigger').on('click', function(event){
    event.preventDefault();
    $('.cd-popup').addClass('is-visible');
  });
  
  //close popup
  $('.cd-popup').on('click', function(event){
    if( $(event.target).is('.cd-popup-close') || $(event.target).is('.cd-popup') ) {
      event.preventDefault();
      $(this).removeClass('is-visible');
    }
  });
  //close popup when clicking the esc keyboard button
  $(document).keyup(function(event){
      if(event.which=='27'){
        $('.cd-popup').removeClass('is-visible');
      }
  });
}