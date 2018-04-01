$(function() {
  var sketch = $('#sketch').sketch();
});

$('#recognizeBtn').on('click', function (e) {
  var canvas = document.getElementById('sketch');
  $.ajax({
    type: "POST",
    url: '/recognizer',
    data: JSON.stringify({'image':canvas.toDataURL()}),
    contentType: "application/json; charset=utf-8",
  }).done(function(data) {
      console.log(data);
      var text = $('#digit').text();
      $('#digit').text('Recognized digit: '+data)
  });
});

$('#clearBtn').on('click', function (e) {
  var canvas = document.getElementById('sketch');
  var context = canvas.getContext('2d');
  context.clearRect(0, 0, canvas.width, canvas.height);
  $('#sketch').sketch('actions',[]);
  $('#digit').text('');
 });