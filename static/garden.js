/*function startup(time, temp, humi) {
    if (localStorage.getItem("graphlocal") === null) {
        // Retrieve
        charttemp(time, temp, humi);
    } else if (localStorage.getItem("graphlocal") === "humi") {
        charthumi(time, humi);
    } else {
        charttemp(time, temp, humi);
    }
}

function localtemp() {
    localStorage.setItem("graphlocal", "temp");
    location.reload();
}

function localhumi() {
    localStorage.setItem("graphlocal", "humi");
    location.reload();
}*/

function graph(time, temp, column) {

    var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: time,
        datasets: [{
			      backgroundColor: '#00ff00',
            label: column[0],
            data: temp[0],
			fill: false
            }]
		}
});

	function addData(chart, label, color, data){
	
		for(i=1; i < data.length; i++){
			chart.data.datasets.push({
			label: label[i],
			backgroundColor: color,
			data: data[i],
			fill: false
			})};
	chart.update();
}

addData(myChart, column, '#ff0000', temp);

}


	