var linguafaq = {

    expandFaqItemAnswer: function() {
        $('.portlet-collection-faq .portletItem a').prepOverlay({
            subtype: 'ajax'
            })
    } // no comma after last item

}

$(document).ready(function() {
    linguafaq.expandFaqItemAnswer();
});

