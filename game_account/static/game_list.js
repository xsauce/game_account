function load_game_data(){
    jQuery.ajax({
        type: "GET",
        url: "games",
        dataType: "json",
        success: function(data, status){
            $("#game-list-table tbody").html('');
            for(var i=0;i<data.data.length;i++){
                $("#game-list-table tbody").append(
                "<tr class=" + (data.data[i].game_status == 1 ? "" : "table-danger") + ">" +
                "<td>" + data.data[i].game_id + "</td>" +
                "<td>" + data.data[i].game_finish_datetime + "</td>" +
                "<td>" + data.data[i].score_to_money_rate + "</td>" +
                "<td>" + (data.data[i].game_status == 1 ? '已结算': '未结算') + "</td>" +
                "<td>" + data.data[i].player1_id + "</td>" +
                "<td>" + data.data[i].player1_score + "</td>" +
                "<td>" + data.data[i].player2_id + "</td>" +
                "<td>" + data.data[i].player2_score + "</td>" +
                "<td>" + data.data[i].player3_id + "</td>" +
                "<td>" + data.data[i].player3_score + "</td>" +
                "<td>" + data.data[i].player4_id + "</td>" +
                "<td>" + data.data[i].player4_score + "</td>" +
                (data.data[i].game_status == 1 ? "<td></td>" : "<td><button type='button' class='btn btn-link edit-btn' data='" + JSON.stringify(data.data[i]) + "'>编辑</button>" +
                "<button type='button' class='btn btn-link del-btn' data='" + data.data[i].game_pkid + "'>删除</button></td>") +
                "</tr>")
            }
            $("#game-list-table .edit-btn").on('click', function(){
                edit_game_info(JSON.parse($(this).attr("data")));
            })

            $("#game-list-table .del-btn").on('click', function(){
                del_game_info($(this).attr("data"));
            })
        }
    });
}


function edit_game_info(game_info){
    $("#e-submit-error").hide();
    $("#e-game-pkid-input").val(game_info.game_pkid)
    $("#e-game-id-input").val(game_info.game_id);
    $("#e-score-to-money-rate-input").val(game_info.score_to_money_rate);
    $("#e-game-finish-datetime-input").val(game_info.game_finish_datetime.replace(' ', 'T'));
//    $("#e-game-status-input").val(game_info.game_status);
    for(var i=1;i<=4;i++){
        $("#e-player" + i + "-id-input").val(game_info["player" + i + '_id']);
        $("#e-player" + i + "-score-input").val(game_info["player" + i + '_score']);
    }
    $("#editOneModal").modal("show");
}

function add_one(){
    req_data = {
        game_id:$.trim($("#game-id-input").val()),
        score_to_money_rate: $.trim($("#score-to-money-rate-input").val()),
        result: []
    };
    for(var i=1;i<=4;i++){
        req_data.result.push({
           player_id: $.trim($("#player" + i + "-id-input").val()),
           player_score: $.trim($("#player" + i + "-score-input").val()).replace('－', '-')
        })
    }
    jQuery.ajax({
        type: 'POST',
        url:"add_game",
        dataType: 'json',
        data: JSON.stringify(req_data),
        success: function(data, status){
            if(data.code != 0){
                $("#submit-error").show();
                $("#submit-error").html(data.msg);
            }
            else{
                $("#addOneModal").modal('hide');
                clear_submit_data();
                load_game_data();
            }
        }
    });
}

function edit_one(){
    req_data = {
        game_pkid: $("#e-game-pkid-input").val(),
        game_id:$.trim($("#e-game-id-input").val()),
        game_finish_datetime: $.trim($("#e-game-finish-datetime-input").val()).replace('T', ' '),
//        game_status: $.trim($("#e-game-status-input").val()),
        score_to_money_rate: $.trim($("#e-score-to-money-rate-input").val()),
        result: []
    };
    for(var i=1;i<=4;i++){
        req_data.result.push({
           player_id: $.trim($("#e-player" + i + "-id-input").val()),
           player_score: $.trim($("#e-player" + i + "-score-input").val()).replace('－', '-')
        })
    }
    jQuery.ajax({
        type: 'POST',
        url: "edit_game",
        dataType: 'json',
        data: JSON.stringify(req_data),
        success: function(data, status){
            if(data.code != 0){
                $("#e-submit-error").show();
                $("#e-submit-error").html(data.msg);
            }
            else{
                $("#editOneModal").modal('hide');
                load_game_data();
            }
        }
    });
}

function del_game_info(game_pkid){
    $("#del-game-pkid-input").val(game_pkid)
    $("#delOneModal").modal("show");
}

function del_one(){
    req_data = {
        game_pkid: $("#del-game-pkid-input").val()
    }
    jQuery.ajax({
        type: 'POST',
        url: "del_game",
        dataType: 'json',
        data: req_data,
        success: function(data, status){
            $("#delOneModal").modal('hide');
            if(data.code != 0){
                show_tip(data.msg);
            }
            else{
                load_game_data();
            }
        }
    });

}

function clear_submit_data(){
    $("#submit-error").hide();
    $("#addOneForm input").val('');
    $("#score-to-money-rate-input").val("30");
}

function close_bill(){
    req_data = {
        fee_rate: $.trim($("#fee-rate-input").val()),
        close_bill_check_point: $("#close-bill-check-point-input").val().replace("T", " ")
    }
    $.ajax({
        url: "close_bill",
        type: "POST",
        data: req_data,
        dataType: "json",
        success: function(data, status){
            $("#closeBillModal").modal("hide");
            if(data.code != 0){
                show_tip(data.msg);
            }
            else{
                show_tip("结算成功");
                load_game_data();
            }
        }
    });
}

function show_tip(msg){
    $("#tip #tip-show-text").html(msg);
    $("#tip").modal('show');
}

function get_now(){
    var d = new Date();
    var datestring = d.getFullYear() + "-" + ("0"+(d.getMonth()+1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2)
     + "T" + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2) + ":" + ("0" + d.getSeconds()).slice(-2);
    return datestring;
}

function show_close_bill_modal(){
    $("#close-bill-check-point-input").val(get_now())
}

$(document).ready(function(){
    load_game_data();

    $("#addOneBtn").on('click', add_one);

    $('#addOneModal').on('hide.bs.modal', function(e){
        clear_submit_data();
    });

    $("#submitCloseBillBtn").on('click', close_bill);

    $("#submit-error").hide();
    $("#editOneBtn").on('click', edit_one)
    $("#delOneBtn").on('click', del_one)

    $("#closeBillModal").on('show.bs.modal', function(e){
        show_close_bill_modal();
    });
});