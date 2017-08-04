/**
 * Created by admin on 24.07.17.
 */
$(function(){
    $('.inline-group .inline-related .delete input').each(function(i,e){
        $(e).bind('change', function(e){
            if(this.checked) {
                // marked for deletion
                $(this).parents('.inline-related').children('fieldset.module').addClass('collapsed collapse')
            }else{
                $(this).parents('.inline-related').children('fieldset.module').removeClass('collapsed')
            }
        })
    })
})