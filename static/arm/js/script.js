function get_date(d){
    var d = new Date();
    var day = d.getDate();
    var monthes = [01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12]
    var month = monthes[d.getMonth()];
    var year = d.getFullYear();
    return year + '.' + month + '.' + day;
}

$(document).ready(function() {
    $('#end_date').val(get_date);
 });
