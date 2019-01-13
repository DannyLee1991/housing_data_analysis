// 用户获取绘图结果的ajax请求
function ajaxForView(locate_a, locate_b, start, end, what, callback) {
    $.ajax({
        url: "/views/plot_distribution",
        type: 'post',
        data: {
            locate_a: locate_a,
            locate_b: locate_b,
            start: start,
            end: end,
            what: what
        },
        dataType: "html",
        success: function (data, status) {
            callback(data, status);
        }
    });
}

function ajaxForAreaDistribution(locate_a = '', locate_b = '', start = 0, end = 0) {
    ajaxForView(locate_a, locate_b, start, end, "AREA", function (data, status) {
        $('#plot_area_distribution').html(data);
    });
}

function ajaxForPriceDistribution(locate_a = '', locate_b = '', start = 0, end = 0) {
    ajaxForView(locate_a, locate_b, start, end, "PRICE", function (data, status) {
        $('#plot_price_distribution').html(data);
    });
}

function ajaxForUnitPriceDistribution(locate_a = '', locate_b = '', start = 0, end = 0) {
    ajaxForView(locate_a, locate_b, start, end, "UNIT_PRICE", function (data, status) {
        $('#plot_unit_price_distribution').html(data);
    });
}

function ajaxForBuildTimeDistribution(locate_a = '', locate_b = '', start = 0, end = 0) {
    ajaxForView(locate_a, locate_b, start, end, "BUILD_TIME_INFO", function (data, status) {
        $('#plot_build_time_distribution').html(data);
    });
}

function loadPlot(locat_a = '', locat_b = '', start = 0, end = 0) {
    ajaxForAreaDistribution(locat_a, locat_b, start, end);
    ajaxForPriceDistribution(locat_a, locat_b, start, end);
    ajaxForUnitPriceDistribution(locat_a, locat_b, start, end);
    ajaxForBuildTimeDistribution(locat_a, locat_b, start, end);
}
