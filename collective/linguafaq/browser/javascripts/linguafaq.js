var linguafaq = {
    expandFaqItemAnswer: function() {
        $('.portlet-collection-faq .portletItem a').prepOverlay({
            subtype: 'ajax'
        });
    }
};
$(document).ready(function() {
    linguafaq.expandFaqItemAnswer();
});
