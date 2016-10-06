// initialize variables
var request_responses_reload_index = 0;
var request_responses_index = 0;
var request_responses;
var request_responses_index_shift = 10;

// hide load-more-responses div
$(".load-more-responses").hide();

// loads initial responses into div
$(document).ready(function () {
    $.ajax({
        type: "POST",
        url: '/request/api/v1.0/responses',
        data: {request_responses_reload_index: request_responses_reload_index},
        success: function (data) {
            request_responses = data.request_responses;
            var request_responses_html = '<table class="table"> <tbody>';
            for (var i = request_responses_index; i < request_responses_index + request_responses_index_shift; i++) {
                request_responses_html = request_responses_html + '<tr> <td>' + request_responses[i] + '<button style="float: right;" type="button" class="btn btn-secondary btn-sm">Edit</button> </td> </tr>';
            }
            document.getElementById("request-responses-table").innerHTML = request_responses_html;
        },
        error: function (error) {
            console.log(error);
        }
    });
});

// replaces currently displayed responses with previous 10 responses
function previous_responses() {
    if (request_responses_index != 0) {
        request_responses_index = request_responses_index - request_responses_index_shift;
        var request_responses_html = '<table class="table"> <tbody>';
        for (var i = request_responses_index; i < request_responses_index + request_responses_index_shift; i++) {
            request_responses_html = request_responses_html + '<tr> <td>' + request_responses[i] + '<button style="float: right;" type="button" class="btn btn-secondary btn-sm">Edit</button> </td> </tr>';
        }
        document.getElementById("request-responses-table").innerHTML = request_responses_html;
    }
    if (request_responses_index == request_responses.length - request_responses_index_shift) {
        $(".load-more-responses").show();
    } else {
        $(".load-more-responses").hide();
    }
}

// replaces currently displayed responses with next 10 responses
function next_responses() {
    if (request_responses_index != request_responses.length - request_responses_index_shift) {
        request_responses_index = request_responses_index + request_responses_index_shift;
        var request_responses_html = '<table class="table"> <tbody>';
        for (var i = request_responses_index; i < request_responses_index + request_responses_index_shift; i++) {
            request_responses_html = request_responses_html + '<tr> <td>' + request_responses[i] + '<button style="float: right;" type="button" class="btn btn-secondary btn-sm">Edit</button> </td> </tr>';
        }
        document.getElementById("request-responses-table").innerHTML = request_responses_html;
    }
    if (request_responses_index == request_responses.length - request_responses_index_shift) {
        $(".load-more-responses").show();
    } else {
        $(".load-more-responses").hide();
    }
}

// loads 50 more responses into request_responses array
function load_more_responses() {
    request_responses_reload_index++;
    $.ajax({
        type: "POST",
        url: '/request/api/v1.0/responses',
        data: {request_responses_reload_index: request_responses_reload_index},
        success: function (data) {
            request_responses = data.request_responses;
            var request_responses_html = '<table class="table"> <tbody>';
            for (var i = request_responses_index; i < request_responses_index + request_responses_index_shift; i++) {
                request_responses_html = request_responses_html + '<tr> <td>' + request_responses[i] + '<button style="float: right;" type="button" class="btn btn-secondary btn-sm">Edit</button> </td> </tr>';
            }
            document.getElementById("request-responses-table").innerHTML = request_responses_html;
        },
        error: function (error) {
            console.log(error);
        }
    });
    $(".load-more-responses").hide();
}