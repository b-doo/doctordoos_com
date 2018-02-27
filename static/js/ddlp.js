(function() {
    'use strict';

    jQuery(document).on('scroll', function() {
        if (jQuery(document).scrollTop() > 100) {
            jQuery('img#img-cbd-banner').addClass('banner-small');
        } else {
            jQuery('img#img-cbd-banner').removeClass('banner-small');
        }
    });
})();