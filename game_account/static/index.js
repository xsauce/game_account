function load_game_list_html(){
    $("#nav-ul-btn li a").removeClass("active");
    $("#game-list-btn").addClass("active");
    $("#main-container").load('game_list');
}

function load_close_bill_history_html(){
    $("#nav-ul-btn li a").removeClass("active");
    $("#close-bill-history-btn").addClass("active");
    $("#main-container").load('close_bill_history');
}

$(document).ready(function(){
    $("#game-list-btn").on('click', function(){
        load_game_list_html();
    });

    $("#close-bill-history-btn").on('click', function(){
        load_close_bill_history_html();
    });
});