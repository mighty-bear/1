;(function($){
    "use strict";
    /*-------------------------------------------------------------------------------
	  Navbar 
	-------------------------------------------------------------------------------*/

	//* Navbar Fixed  
    function navbarFixed(){
        if ( $('#fixed_top').length ){ 
            $(window).scroll(function() {
                var scroll = $(window).scrollTop();   
                if (scroll){
                    $("#fixed_top").addClass("navbar_fixed");
                } else {
                    $("#fixed_top").removeClass("navbar_fixed");
                }
            });
        };
    };
    navbarFixed();
    
    var nav_offset_top = $('.header_two').height()+10; 
    /*-------------------------------------------------------------------------------
	  Navbar 
	-------------------------------------------------------------------------------*/

	//* Navbar Fixed  
    function navbarFixeds(){
        if ( $('#stricky').length ){ 
            $(window).scroll(function() {
                var scroll = $(window).scrollTop();   
                if (scroll >= nav_offset_top ) {
                    $("#stricky").addClass("navbar_fixed");
                } else {
                    $("#stricky").removeClass("navbar_fixed");
                }
            });
        };
    };
    navbarFixeds();
    
    /* ===== Parallax Effect===== */
	function parallaxEffect() {
        if($('.parallax-effect').length){
            $('.parallax-effect').parallax();
        };
	}
    parallaxEffect();
    
    
    /*===========Start Service Slider js ===========*/
    function stTestimonialSlider(){
        var testimonial_slider = $("#t_slider");
        if( testimonial_slider.length ){
            testimonial_slider.owlCarousel({
                loop:true,
                margin:0,
                items: 2,
                autoplay: true,
                smartSpeed: 2000,
                responsiveClass:true,
                nav: false,
                dots: true,
                stagePadding: 320,
                responsive:{
                    0:{
                        items:1,
                        stagePadding: 0,
                    },
                    690:{
                        items:2,
                        stagePadding: 0,
                    },
                    992:{
                        items:2, 
                        stagePadding: 80,
                    },
                    1199:{
                        items:2, 
                        stagePadding: 100,
                    },
                    1300:{
                        items:2,
                        stagePadding: 200,
                    }, 
                    1500:{
                        items:2,  
                        stagePadding: 320,
                    }
                },
            })
        }
    }
    stTestimonialSlider();
    
    function bTestimonialSlider(){
        var test_slider = $("#t_slider_two");
        if( test_slider.length ){
            test_slider.owlCarousel({
                loop:true,
                margin:0,
                items: 3,
                autoplay: true,
                smartSpeed: 2000,
                responsiveClass:true,
                nav: false,
                dots: true,
                responsive:{
                    0:{
                        items:1, 
                    },
                    578:{
                        items:1, 
                    },
                    750:{
                        items:2, 
                    },
                    992:{
                        items:3,
                    }, 
                    1200:{
                        items:3,   
                    }
                },
            })
        }
    }
    bTestimonialSlider();
    
    
    function bTestimonialSliderTwo(){
        var testSlider = $("#t_slider_three");
        if( testSlider.length ){
            testSlider.owlCarousel({
                loop:true,
                margin:0,
                items: 2,
                autoplay: true,
                smartSpeed: 2000,
                responsiveClass:true,
                nav: false,
                dots: true,
                responsive:{
                    0:{
                        items:1, 
                    },
                    768:{
                        items:2,
                    }
                },
            })
        }
    }
    bTestimonialSliderTwo();
    
    function agencyT(){
        var agencyTestimonial = $("#agency_slider");
        if( agencyTestimonial.length ){
            agencyTestimonial.owlCarousel({
                loop:true,
                margin:150,
                items: 2,
                autoplay: true,
                smartSpeed: 2000,
                responsiveClass:true,
                nav: false,
                dots: true,
                responsive:{
                    0:{
                        items:1, 
                        margin: 30
                    },
                    768:{
                        items:1, 
                        margin: 30
                    },
                    992:{
                        items:2,
                        margin: 50
                    },
                    1199:{
                        items:2,
                        margin: 300
                    }
                },
            })
        }
    }
    agencyT();
    
    function agencySlider(){
        var agencyS = $(".agency_slider")
        if(agencyS.length){
            agencyS.owlCarousel({
                loop:true,
                margin:30,
                items: 5,
                autoplay: true,
                smartSpeed: 2000,
                responsiveClass:true,
                nav: false,
                dots: true,
                responsive:{
                    0:{
                        items:1
                    },
                    576:{
                        items:2
                    },
                    768:{
                        items:3 
                    },
                    992:{
                        items:4
                    },
                    1199:{
                        items:5
                    }
                },
                
            })
        }
    }
    agencySlider();
    
    
      $('.main_slider').on('init', function (e, slick) {
          var $firstAnimatingElements = $('div.slider_item:first-child').find('[data-animation]');
          doAnimations($firstAnimatingElements);
      });
      $('.main_slider').on('beforeChange', function (e, slick, currentSlide, nextSlide) {
          var $animatingElements = $('div.slider_item[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
          doAnimations($animatingElements);
      });
      $('.main_slider').slick({
          autoplay: true,
          autoplaySpeed: 8000,
          speed: 2000,
          dots: false,
          fade: true,
          prevArrow: ".left_arrow",
          nextArrow: ".right_arrow",
      });

      function doAnimations(elements) {
          var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
          elements.each(function () {
              var $this = $(this);
              var $animationDelay = $this.data('delay');
              var $animationType = 'animated ' + $this.data('animation');
              $this.css({
                  'animation-delay': $animationDelay,
                  '-webkit-animation-delay': $animationDelay
              });
              $this.addClass($animationType).one(animationEndEvents, function () {
                  $this.removeClass($animationType);
              });
          });
      }
    
    /*===========Portfolio isotope js===========*/
    function portfolioMasonry(){
        var portfolio = $("#work-portfolio");
        if( portfolio.length ){
            portfolio.imagesLoaded( function() {
              // images have loaded
                // Activate isotope in container
                portfolio.isotope({
                    itemSelector: '.portfolio_item',
                    layoutMode: 'masonry',
                    masonry: {
                        // use outer width of grid-sizer for columnWidth
                        columnWidth: '.grid-sizer'
                    },
                    animationOptions :{
                        duration:1000
                    },
                    hiddenStyle: {
                        opacity: 0,
                        transform: 'scale(.4)rotate(60deg)',
                    },
                    visibleStyle: {
                        opacity: 1,
                        transform: 'scale(1)rotate(0deg)',
                    },
                    stagger: 0,
                    transitionDuration: '0.5s',
                });

                // Add isotope click function
                $("#portfolio_filter div").on('click',function(){
                    $("#portfolio_filter div").removeClass("active");
                    $(this).addClass("active");

                    var selector = $(this).attr("data-filter");
                    portfolio.isotope({
                        filter: selector,
                        animationOptions: {
                          animationDuration: 750,
                          easing: 'linear',
                          queue: false
                      }
                    })
                    return false;
                })
            })
        }
    }
    portfolioMasonry();
    
    //    progress-bar....//
    $(".progress-element").each(function() {
        $(this).waypoint(function() {
            var progressBar = $(".progress-bar");
            progressBar.each(function(indx){
                $(this).css("width", $(this).attr("aria-valuenow") + "%")
            })
        }, {
            triggerOnce: true,
            offset: 'bottom-in-view',
        });
    });
    
    /* Counter Js */
    function counterUp(){
        if ( $('.counter').length ){ 
            $('.counter').counterUp({
                delay: 1,
                time: 250
            });
        };
    };  
    
    counterUp();
    
    $(".project").hover3d({
        selector: ".project__card",
        shine: true,
        sensitivity: 12,
    });
    
    /*--------------- End popup-js--------*/
    function popupGallery(){
        if ($(".img_popup").length) {
            $(".img_popup").each(function(){
                $(".img_popup").magnificPopup({
                    type: 'image',
                    tLoading: 'Loading image #%curr%...',
                    removalDelay: 300,
                    mainClass:  'mfp-with-zoom mfp-img-mobile',
                    gallery: {
                        enabled: true,
                        navigateByImgClick: true,
                        preload: [0,1] // Will preload 0 - before current, and 1 after the current image,
                    }
                });
            })
        }
        if($('.popup-youtube').length){
            $('.popup-youtube').magnificPopup({
                disableOn: 700,
                type: 'iframe',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: false,
                mainClass:  'mfp-with-zoom mfp-img-mobile',
            });
        }
    }
    popupGallery();
    
    /*----------------------------------------------------*/
    /*  Google map js
    /*----------------------------------------------------*/
    
    if ( $('#mapBox').length ){
        var $lat = $('#mapBox').data('lat');
        var $lon = $('#mapBox').data('lon');
        var $zoom = $('#mapBox').data('zoom');
        var $marker = $('#mapBox').data('marker');
        var $info = $('#mapBox').data('info');
        var $markerLat = $('#mapBox').data('mlat');
        var $markerLon = $('#mapBox').data('mlon');
        var map = new GMaps({
        el: '#mapBox',
        lat: $lat,
        lng: $lon,
        scrollwheel: false,
        scaleControl: true,
        streetViewControl: false,
        panControl: true,
        disableDoubleClickZoom: true,
        mapTypeControl: false,
        zoom: $zoom,
            styles: [
                {
                    "featureType": "administrative.country",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "visibility": "simplified"
                        },
                        {
                            "hue": "#ff0000"
                        }
                    ]
                }
            ]
        });

        map.addMarker({
            lat: $markerLat,
            lng: $markerLon,
            icon: $marker,    
            infoWindow: {
              content: $info
            }
        })
    }
    
    /*--------- WOW js-----------*/
    function wowAnimation(){
        new WOW({
            offset: 100,          
            mobile: true
        }).init()
    }
    wowAnimation();
    
    $('.search-btn').on('click', function(){
        $('body').addClass('open');
        setTimeout(function () {
            $('.search-input').focus();
        }, 500);
        return false;
    });
	$('.close_icon').on('click', function(){
		$('body').removeClass('open');
		return false;
	});
    
    function loader(){
        $(window).on('load', function() {
            $('#ctn-preloader').addClass('loaded');
            // Una vez haya terminado el preloader aparezca el scroll

            if ($('#ctn-preloader').hasClass('loaded')) {
                // Es para que una vez que se haya ido el preloader se elimine toda la seccion preloader
                $('#preloader').delay(900).queue(function () {
                    $(this).remove();
                });
            }
        });
    }
    loader();
    
})(jQuery)