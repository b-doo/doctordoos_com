(function() {
    'use strict';

    jQuery(document).on('scroll', function() {
        if (jQuery('body').scrollTop() > 100) {
            jQuery('img#img-cbd-banner').addClass('banner-small');
        } else {
            console.log('lt100');
            jQuery('img#img-cbd-banner').removeClass('banner-small');
        }
    });
})();