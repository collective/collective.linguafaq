var linguafaq = {

    expandForm: function() {
        $('#useful input:radio[value="0"]').click(function() {
            jq(this).parent().find(".comments").fadeIn();
        }); 
    },

    expandFaqItemAnswer: function() {
        $('a.faqItemLink').prepOverlay({
            subtype: 'ajax',
            });
    } // no comma after last item

}

jq(document).ready(function() {
    linguafaq.expandFaqItemAnswer();
    linguafaq.expandForm();
});

