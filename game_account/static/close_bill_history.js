function open_close_bill_detail_modal(data) {
  $("#closeBillHistoryDetailTable tbody").html('');
  detail_data = data.items;
  $("#downloadCloseBillDetail").attr({
    "data": data.history_pkid
  });
  for (var i = 0; i < detail_data.length; i++) {
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


function get_close_bill_history_player_detail(player_id, history_pkid) {
  CommonFunc.ajaxJSON("close_bill_history_player_detail", "POST", {
    player_id: player_id,
    close_bill_history_pkid: history_pkid
  }, function(data) {
    if (data.code != 0) {
      CommonFunc.show_error_msg(data.msg);
    } else {
      $("#closeBillHistoryPlayerDetailTable tbody").empty();
      for (var i = 0; i < data.data.length; i++) {
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
  });
}

function del_close_bill_history_modal(history_pkid) {
  $("#del-history-pkid-input").val(history_pkid);
  $("#delOneModal").modal('show');
}

function del_one() {
  req_data = {
    close_bill_history_pkid: $("#del-history-pkid-input").val()
  }
  CommonFunc.ajaxJSON("del_close_bill_history", "POST", req_data, function(data, status) {
    $("#delOneModal").modal('hide');
    if (data.code != 0) {
      show_tip(data.msg);
    } else {
      load_close_bill_history_data();
    }
  });
}

function load_close_bill_history_data(start_dt, end_dt) {
  if (!start_dt && !end_dt) {
    if (!$("#datetimeRange").val()) {
      start_dt = format_dt_1(new Date(new Date().getTime() - 1 * 24 * 60 * 60 * 1000)).split(' ')[0] + ' 00:00:00';
      end_dt = format_dt_1(new Date()).split(' ')[0] + ' 23:59:59';
    } else {
      date_range_val = $("#datetimeRange").val().split(" - ");
      start_dt = date_range_val[0];
      end_dt = date_range_val[1];
    }
  }

  CommonFunc.ajaxJSON("close_bill_histories_by_created_at", "POST", {
    start_dt: start_dt,
    end_dt: end_dt
  }, function(data, status) {
    if (!data.data) return;
    $("#close-bill-history-table tbody").html('');
    for (var i = 0; i < data.data.length; i++) {
      $("#close-bill-history-table tbody").append(
        "<tr>" +
        "<td>" + data.data[i].close_bill_check_point + "</td>" +
        "<td>" + data.data[i].fee_rate + "</td>" +
        //                "<td>" + data.data[i].total_final_money + "</td>" +
        "<td>" + data.data[i].total_money + "</td>" +
        "<td>" + data.data[i].total_fee + "</td>" +
        "<td>" + data.data[i].total_game_count + "</td>" +
        "<td><button type='button' class='btn btn-link re-check' data='" + data.data[i].history_pkid + "'>重算</button>" +
        "<button type='button' class='btn btn-link detail' data='" + JSON.stringify(data.data[i]) + "'>详情</button>" +
        "<button type='button' class='btn btn-link del' data='" + data.data[i].history_pkid + "'>删除</button></td>" +
        "</tr>");
    }
    $("#close-bill-history-table .detail").on('click', function() {
      open_close_bill_detail_modal(JSON.parse($(this).attr("data")));
    });
    $("#close-bill-history-table .del").on('click', function() {
      del_close_bill_history_modal($(this).attr("data"));
    })
  });
}


function download_csv() {
  history_pkid = $(this).attr("data");
  window.open('download_close_bill_history_detail?game_type_pkid=' + $("#game_type_pkid_hidden").val() + '&close_bill_history_pkid=' + history_pkid, '_blank');
}

$(document).ready(function() {
  load_close_bill_history_data();
  $("#delOneBtn").on('click', del_one);
  $("#downloadCloseBillDetail").on('click', download_csv);
  $("#datetimeRange").daterangepicker({
    timePicker: true,
    timePickerIncrement: 30,
    "timePicker24Hour": true,
    locale: {
      format: 'YYYY-MM-DD HH:mm:ss'
    },
    "startDate": format_dt_1(new Date(new Date().getTime() - 1 * 24 * 60 * 60 * 1000)).split(' ')[0] + ' 00:00:00',
    "endDate": format_dt_1(new Date()).split(' ')[0] + ' 23:59:59'
  }, function(st, et, label) {
    load_close_bill_history_data(st.format('YYYY-MM-DD HH:mm:ss'), et.format('YYYY-MM-DD HH:mm:ss'));
  });
});
