var linguafaq = {

    expandFaqItemAnswer: function() {
        $('a.faqItemLink').prepOverlay({
            subtype: 'ajax',
            });
    } // no comma after last item

}

jq(document).ready(function() {
    linguafaq.expandFaqItemAnswer();
});

