$(document).ready(function () {
  $(".list-group-item").click(function () {
    const keyname = $(this).attr("id");

    const url = "http://127.0.0.1:5000/detail?title=" + keyname;

    $.get(url).then(function (data) {
      $("#detailModalLabel").text(data.title);
      $("#detailModalContent").text(data.content);
      $("#detailModal").modal("show");
    });
  });
});

$(".list-button").click(function () {
  location.href = "/edit";
});
