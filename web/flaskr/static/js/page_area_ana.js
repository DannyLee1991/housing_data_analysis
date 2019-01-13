var strAll = "全部";

function loadLocateA() {
    $.ajax({
        url: "/api/locate/a",
        type: 'get',
        dataType: "json",
        success: function (data, status) {
            let r = "";
            r += ("<li><a href=\"#\" onclick='onChooseLocateA(\"全部\")'>全部</a></li>");
            data.data.forEach(v => {
                r += ("<li><a href=\"#\" onclick='onChooseLocateA(\"" + v + "\")'>" + v + "</a></li>");
            });
            $("#ul-locate-a").html(r);
        }
    });
}

function loadLocateB(locateA) {
    $.ajax({
        url: "/api/locate/b",
        type: 'get',
        data: {locate_a: locateA},
        dataType: "json",
        success: function (data, status) {
            let r = "";
            r += ("<li><a href=\"#\" onclick='onChooseLocateB(\"全部\")'>全部</a></li>");
            data.data.forEach(v => {
                r += ("<li><a href=\"#\" onclick='onChooseLocateB(\"" + v + "\")'>" + v + "</a></li>");
            });
            $("#ul-locate-b").html(r);
        }
    });
}

function refresh() {

    let locate_a_val = $("#ip_locate_a").val();
    let locate_b_val = $("#ip_locate_b").val();

    if (locate_a_val == "全部" || locate_a_val == "") {
        $("#bt-locate-a").html("全部" + "<span class=\"caret\"></span>");
        loadPlot();
    } else {
        $("#bt-locate-a").html(locate_a_val + "<span class=\"caret\"></span>");
        if (locate_b_val == "全部" || locate_b_val == "") {
            $("#bt-locate-b").html("全部" + "<span class=\"caret\"></span>");
            loadPlot(locate_a_val);
        } else {
            $("#bt-locate-b").html(locate_b_val + "<span class=\"caret\"></span>");
            loadPlot(locate_a_val, locate_b_val);
        }
    }
}

function onChooseLocateA(locateA) {
    $("#ip_locate_a").val(locateA);

    $("#ip_locate_b").val("全部");

    loadLocateB(locateA);
    refresh();
}

function onChooseLocateB(locateB) {
    $("#ip_locate_b").val(locateB);

    refresh();
}

$(function () {
    loadLocateA();
    refresh();
});