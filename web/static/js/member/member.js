;
var member_set_ops = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        var that = this
        $(".wrap_member_set .save").click(function () {
            $(".wrap_member_set").submit();
        })
    }
};
$(document).ready(function () {
        member_set_ops.init();
});