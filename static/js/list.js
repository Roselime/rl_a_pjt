$(document).ready(function () {
  $(".list-group-item").click(function () {
    const keyname = $(this).attr("id");

    const url = "/detail?title=" + keyname;
    console.log(url);

    $.get(url).then(function (data) {
      console.log(data);
      $("#detailModalLabel").text(data.title);
      $("#detailModalContent").text(data.content);
      console.log("clickpost");
      $("#detailModal").modal("show");
    });
  });
});

$(".list-button").click(function () {
  location.href = "/edit";
});
