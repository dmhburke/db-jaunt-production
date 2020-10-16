$(document).ready(function() {

  $("#showMatchReportButton").click(function() {
    // $(this).siblings("#matchReportContainer").css("visibility", "visible");
    $("#matchReportContainer").css("display", "block");

  });

  $("#showResults").click(function() {
    $(this).siblings("#resultsCollapse").toggleClass("show");
  });

  $("#showReport").click(function() {
    $(this).siblings("#reportCollapse").toggleClass("show");
  });

  $("#showNewscast").click(function() {
    $(this).siblings("#newscastCollapse").toggleClass("show");
  });

  // Match reports: Delay link being visible for estimated amount of time
  setTimeout(function(){
    $("#matchReportFileButton").css("visibility", "visible");
  }, 15000);


  //END DOC READY FUNCTION
  });
