// For explore 
$('.explore').on('click', function(){
    document.querySelector('.explore-target').scrollIntoView({behavior: "smooth"});
});

// For nav search bar btw 900px to 600px
$('.sm-input').hide();

$('.sm-search-icon').on('click', function() {
    $('.sm-toggle__icon').toggleClass('fa-search-plus').toggleClass('fa-search-minus');
    $('.sm-input').slideToggle();
});

// For footer copyright Year
let date = new Date();
let year = date.getFullYear();
$('#copyrightYear').text(year);


// Filter menu toggle
$('.r-head').click(function(){
    $(this).next().slideToggle('fast');
});

// For Heart & popUp
function popUp(){
    $('.fav-pop').show().delay(500).fadeOut('slow');
}
$('.fav-me').on('click', function(){
    console.log($(this).next());
    $(this).children().toggleClass('far').toggleClass('fas');

    if($(this).children().attr('class').includes('fas')){
        $('.fav-pop__message').text('Added to favorites!');
        popUp();
    }else{
        $('.fav-pop__message').text('Removed from favorites!');
        popUp();
    };
});
