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
  //open rules popup
  $('.rules-trigger').on('click', function(event){
    event.preventDefault();
    $('.rules-popup').addClass('is-visible');
  });
  
  //close rules popup
  $('.rules-popup').on('click', function(event){
    if( $(event.target).is('.rules-popup-close') || $(event.target).is('.rules-popup') ) {
      event.preventDefault();
      $(this).removeClass('is-visible');
    }
  });
  //close rules popup when clicking the esc keyboard button
  $(document).keyup(function(event){
      if(event.which=='27'){
        $('.rules-popup').removeClass('is-visible');
      }
  });
  
  //open about popup
  $('.about-trigger').on('click', function(event){
    event.preventDefault();
    $('.about-popup').addClass('is-visible');
  });
  
  //close about popup
  $('.about-popup').on('click', function(event){
    if( $(event.target).is('.about-popup-close') || $(event.target).is('.about-popup') ) {
      event.preventDefault();
      $(this).removeClass('is-visible');
    }
  });
  //close about popup when clicking the esc keyboard button
  $(document).keyup(function(event){
      if(event.which=='27'){
        $('.about-popup').removeClass('is-visible');
      }
  });
}
