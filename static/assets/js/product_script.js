$(document).ready(function() {

  $('.color-choose img').on('click', function() {
      console.log(1)
      var headphonesColor = $(this).attr('src');
      console.log(headphonesColor)
      $('.active').removeClass('active');
      document.querySelector("img[src*='"+headphonesColor+"']").classList.add('active');
      $(this).addClass('active');
  });

});
