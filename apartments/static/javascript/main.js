$('.ui.dropdown')
  .dropdown()
;



$(document).ready(function(){
  $('.your-class').slick({
      dots: true,
      infinite: true,
      speed: 500,
      fade: true,
      cssEase: 'linear',
      autoplay: true,
      autoplaySpeed: 1500
  });
});
