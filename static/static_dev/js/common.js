jQuery(function(){

  //вешаем плагин на контейнер-картинку
    $(".my-foto-container").imagezoomsl({
      zoomrange: [1, 12],
      zoomstart: 3,
      innerzoom: true,
      magnifierborder: "none"
    });

  //клик по превью-картинке
    $(".my-foto").click(function(){

       var that = this;

     //копируем атрибуты из превью-картинки в контейнер-картинку
       $(".my-foto-container").fadeOut(600, function(){

         $(this).attr("src",              $(that).attr("src"))              // путь до small картинки
                .attr("data-large",       $(that).attr("data-large"))       // путь до big картинки

                //дополнительные атрибуты, если есть
                //.attr("data-title",       $(that).attr("data-title"))       // заголовок подсказки
                //.attr("data-help",        $(that).attr("data-help"))        // текст подсказки
                //.attr("data-text-bottom", $(that).attr("data-text-bottom")) // текст снизу картинки

                .fadeIn(1000);
       });
   });
});
$( document ).ready(function(){
  $('.ui.dropdown')
    .dropdown({
      // you can use any ui transition
      transition: 'drop',
      allowCategorySelection: true
    });

  // $('.ui.search')
  //   .search({
  //     apiSettings: {
  //       url: 'http://textura.kz/'
  //     },
  //     fields: {
  //       url     : 'html_url'
  //     },
  //     minCharacters : 3
  // });

  $('.ui.accordion')
    .accordion()
  ;

  var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        spaceBetween: 30
    });

  var swiper = new Swiper('.swiper-container', {
        pagination: 'swiper-pagination',
        paginationClickable: true,
        nextButton: 'swiper-button-next',
        prevButton: 'swiper-button-prev',
        spaceBetween: 30,
        loop: true,
        slidesPerView: 1,
        autoplay: 5000
    });
});
