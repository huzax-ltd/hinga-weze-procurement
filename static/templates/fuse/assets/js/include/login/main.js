(function () {
    $('document').ready(function () {

        //Preloader
        $(window).on("load", function () {
            preloaderFadeOutTime = 500;

            function hidePreloader() {
                var preloader = $('.load-bar');
                preloader.fadeOut(preloaderFadeOutTime);
            }

            hidePreloader();
        });

        // Prevent default for empty links
        $('[href="#"]').click(function (e) {
            e.preventDefault()
        });

        // Adding data-parent to togglable nav items
        $('#sidenav [data-toggle]').each(function () {
            $(this).attr('data-parent', '#' + $(this).parent().parent().attr('id'));
        });

        /**
         * Trigger window resize to update nvd3 charts
         */
        $('[data-toggle="tab"]').on('shown.bs.tab', function (e) {
            window.dispatchEvent(new Event('resize'));
        });

        /**
         * Enable tooltips everywhere
         */
        $('[data-toggle="tooltip"]').tooltip();

        /**
         * Enable popovers everywhere
         */
        $('[data-toggle="popover"]').popover();

        // Activate animated progress bar
        $('.bd-toggle-animated-progress').on('click', function () {
            $(this).siblings('.progress').find('.progress-bar-striped').toggleClass('progress-bar-animated')
        });

        /**
         * Enable Custom Scrollbars only for desktop
         */
        var mobileDetect = new MobileDetect(window.navigator.userAgent);

        if (!mobileDetect.mobile()) {
            $('.custom-scrollbar').each(function () {
                new PerfectScrollbar(this);
            })
        } else {
            $('body').addClass('is-mobile');
        }

        /**
         * Fix code block indentations
         */
        $('code').each(function () {
            var lines = $(this).html().split('\n');

            if (lines[0] === '') {
                lines.shift()
            }

            var matches;
            var indentation = (matches = /^\s+/.exec(lines[0])) !== null ? matches[0] : null;

            if (!!indentation) {
                lines = lines.map(function (line) {
                    return line.replace(indentation, '');
                });

                $(this).html(lines.join('\n').trim());
            }
        });

        /**
         * Flip source-preview cards
         */
        $('.toggle-source-preview').on('click', function () {
            $(this).parents('.example').toggleClass('show-source');
        });
    });

})();