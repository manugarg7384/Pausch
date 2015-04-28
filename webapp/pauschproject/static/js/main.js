$(function() {
  init();
  bindButtons($('.wrap button'));

  var REFRESH_INTERVAL = 300;
  window.setInterval(updateButtons, REFRESH_INTERVAL);
});

function updateButtons() {
  $.ajax({
    url: '/update',
    method: 'GET',
    dataType: 'html',
    success: success
  });
}

function bindButtons(buttons) {
  buttons.click(function() {
    console.log('clicked');
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
  });
}

/**
 * Success function for AJAX calls. Updates the buttons on the home page with
 * the new buttons states.
 */
function success(data) {
  var old = $('.wrap button');
  old.unbind('click');
  var newest = $.parseHTML($.trim(data));
  bindButtons($(newest));
  $('.wrap').html(newest);
}

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