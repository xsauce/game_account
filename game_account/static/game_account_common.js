function load_game_list_html() {
  $("#nav-ul-btn li a").removeClass("active");
  $("#game-list-btn").addClass("active");
  $("#main-container").load('game_list');
}

function load_close_bill_history_html() {
  $("#nav-ul-btn li a").removeClass("active");
  $("#close-bill-history-btn").addClass("active");
  $("#main-container").load('close_bill_history');
}

$(document).ready(function() {
  $("#game-list-btn").on('click', function() {
    load_game_list_html();
  });

  $("#close-bill-history-btn").on('click', function() {
    load_close_bill_history_html();
  });
});

CommonFunc = {
  show_error_msg: function(msg) {
    $("#tipDivBody").attr("class", "alert alert-danger").html(msg);
    $("#tipDiv").collapse("show");
  },
  show_tip_msg: function(msg) {
    $("#tipDivBody").attr("class", "alert alert-success").html(msg);
    $("#tipDiv").collapse("show");
  },
  to_obj: function(json_str) {
    try {
      return JSON.parse(json_str);
    } catch (err) {
      return json_str;
    }
  },
  ajaxJSON: function(url, method, data, on_response_func, hide_loading, game_type_pkid) {
    if (hide_loading) {
      $("#loadingModal").modal("show");
    }
    if (!game_type_pkid) {
      game_type_pkid = $("#game_type_pkid_hidden").val();
    }
    $.ajax({
      url: url + '?game_type_pkid=' + game_type_pkid,
      dataType: 'json',
      method: method,
      data: data,
      success: function(data, textStatus, jqXHR) {
        if (hide_loading) {
          $("#loadingModal").modal("hide");
        }
        if (data.code == 400 && data.data.redirect_url) {
          window.location.href = data.data.redirect_url;
        }
        on_response_func(data);
      }
    });
  }
}

function format_dt(d) {
  var datestring = d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2) +
    "T" + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2) + ":" + ("0" + d.getSeconds()).slice(-2);
  return datestring;
}


function format_dt_1(d) {
  var datestring = d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2) +
    " " + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2) + ":" + ("0" + d.getSeconds()).slice(-2);
  return datestring;
}
