const bannerWrapper = $("#frontpage-banner-wrapper")
const bannerImg = $('#banner-image')

$(document).ready(function () {
    bannerSize();
});
$(window).resize(function () {
    bannerSize();
});

function bannerSize() {
    $("#frontpage-banner-wrapper").height(
        0.8 * $(window).height() - $("nav").height()
    );
}

$(document).ready(function () {
    var movementStrength = 10;
    var height = movementStrength / $(window).height();
    var width = movementStrength / $(window).width();

    bannerWrapper.mousemove(function (e) {
        var pageX = e.pageX - ($(window).width() / 2);
        var pageY = e.pageY - ($(window).height() / 2);
        var newvalueX = width * pageX * -1;
        var newvalueY = height * pageY * -1;
        bannerImg.css("object-position", newvalueX + "px     " + newvalueY + "px");
    });
    /* reset
    bannerWrapper.mouseleave(function (e) {
        bannerImg.css("object-position", "50% 50%");
    })
    */
});