$(function() {
  var chart, year, month;

  $('#select-year').change(function() {
    year = this.value;
    refreshChart(year, month);
  });

  $('#select-month').change(function() {
    month = this.value;
    refreshChart(year, month);
  });

  function refreshChart(year, month) {
    if (!year || !month) {
      if (chart) {
        chart.unload();
      }
      return;
    }

    var apiUrl = '/api/temperature/{year}/{month}'
      .replace('{year}', year)
      .replace('{month}', month);

    $('#year-month').text('{month} ({year})'
      .replace('{year}', year)
      .replace('{month}', $('#select-month option:selected').text()))

    $.get(apiUrl, function(data) {
      data.sort(function(t1, t2) { return t1.date.localeCompare(t2.date) });

      chart = c3.generate({
        bindto: '#chart-container',
        data: {
          x: 'x',
          columns: [
            ['x'].concat(data.map(function(t) { return t.date.split('-')[2] })),
            ['min'].concat(data.map(function(t) { return t.min_value })),
            ['max'].concat(data.map(function(t) { return t.max_value }))
          ]
        },
        axis: {
          x: {
              type: 'category'
          }
        }
      });
    });
  }
});
