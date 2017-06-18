function open_close_bill_detail_modal(data){
    $("#closeBillHistoryDetailTable tbody").html('');
    detail_data = data.items;
    $("#downloadCloseBillDetail").attr({"data": data.history_pkid});
    for(var i=0;i<detail_data.length;i++){
        $("#closeBillHistoryDetailTable tbody").append(
        "<tr>" +
        "<td>" + detail_data[i].player_id + "</td>" +
        "<td>" + detail_data[i].final_money + "</td>" +
        "<td>" + detail_data[i].money + "</td>" +
        "<td><button type='button' class='btn btn-link' onclick='get_close_bill_history_player_detail(\"" + detail_data[i].player_id + "\", \"" + data.history_pkid + "\");'>" + detail_data[i].game_count + "</button></td>" +
        "<td>" + detail_data[i].fee + "</td>" +
        "</tr>"
        );
    }
    $("#closeBillHistoryDetailModal").modal("show");
}


function get_close_bill_history_player_detail(player_id, history_pkid){
    show_tip("正在读取...");
    jQuery.ajax({
        type: 'POST',
        url: "close_bill_history_player_detail",
        data: {
            player_id: player_id,
            close_bill_history_pkid: history_pkid
        },
        dataType: 'json',
        success: function(data, status){
            $("#tip").modal('hide');
            if(data.code != 0){
                show_tip(data.msg);
            }
            else{
            $("#closeBillHistoryPlayerDetailTable tbody").empty();
            for(var i=0;i<data.data.length;i++){
                $("#closeBillHistoryPlayerDetailTable tbody").append(
                "<tr>" +
                "<td>" + data.data[i].game_id + "</td>" +
                "<td>" + data.data[i].player_score + "</td>" +
                "<td>" + data.data[i].final_money + "</td>" +
                "<td>" + data.data[i].money + "</td>" +
                "<td>" + data.data[i].fee + "</td>" +
                "</tr>"
                );
            }
            $("#closeBillHistoryPlayerDetailModal").modal("show");

            }

        }
    });
}

function show_tip(msg){
    $("#tip #tip-show-text").html(msg);
    $("#tip").modal('show');
}

function del_close_bill_history_modal(history_pkid){
    $("#del-history-pkid-input").val(history_pkid);
    $("#delOneModal").modal('show');
}

function del_one(){
    req_data = {
        close_bill_history_pkid: $("#del-history-pkid-input").val()
    }
    jQuery.ajax({
        type: 'POST',
        url: "del_close_bill_history",
        dataType: 'json',
        data: req_data,
        success: function(data, status){
            $("#delOneModal").modal('hide');
            if(data.code != 0){
                show_tip(data.msg);
            }
            else{
                load_close_bill_history_data();
            }
        }
    });
}

function load_close_bill_history_data(){
    jQuery.ajax({
        type: "GET",
        url: "close_bill_histories",
        dataType: "json",
        success: function(data, status){
            if(!data.data)return;
            $("#close-bill-history-table tbody").html('');
            for(var i=0;i<data.data.length;i++){
                $("#close-bill-history-table tbody").append(
                "<tr>" +
                "<td>" + data.data[i].close_bill_check_point + "</td>" +
                "<td>" + data.data[i].fee_rate + "</td>" +
//                "<td>" + data.data[i].total_final_money + "</td>" +
                "<td>" + data.data[i].total_money + "</td>" +
                "<td>" + data.data[i].total_fee + "</td>" +
                "<td>" + data.data[i].total_game_count + "</td>" +
                "<td><button type='button' class='btn btn-link re-check' data='" + data.data[i].history_pkid + "'>重算</button>" +
                "<button type='button' class='btn btn-link detail' data='" +  JSON.stringify(data.data[i]) + "'>详情</button>" +
                "<button type='button' class='btn btn-link del' data='" + data.data[i].history_pkid + "'>删除</button></td>" +
                "</tr>");
            }
            $("#close-bill-history-table .detail").on('click', function(){
                open_close_bill_detail_modal(JSON.parse($(this).attr("data")));
            });
            $("#close-bill-history-table .del").on('click', function(){
                del_close_bill_history_modal($(this).attr("data"));
            })
        }
    });
}


function download_csv(){
    history_pkid = $(this).attr("data");
    window.open('download_close_bill_history_detail?close_bill_history_pkid=' + history_pkid, '_blank');
}

$(document).ready(function(){
    load_close_bill_history_data();
    $("#delOneBtn").on('click', del_one)
    $("#downloadCloseBillDetail").on('click', download_csv)
});