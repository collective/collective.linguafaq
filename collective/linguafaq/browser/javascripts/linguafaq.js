var linguafaq = {

    expandFaqItemAnswer: function() {
        $('.portletCollection .portletItem a').prepOverlay({
            subtype: 'ajax',
            });
    } // no comma after last item

}

jq(document).ready(function() {
    linguafaq.expandFaqItemAnswer();
});

