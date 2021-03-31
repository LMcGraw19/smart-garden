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

var colours = ['#3498db', '#28b463','#f1c40f','#2e4053 ','#af7ac5', '#e67e22', '#0b5345', '#7b7d7d', '#138d75']
// If graph needs more than 10 sensors then add more colours


    var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: time,
        datasets: [{
			      backgroundColor: '#FF3300 ',
            label: column[0],
            data: temp[0],
			fill: false,
			borderColor: '#FF3300 '
            }]
		}
});

	function addData(chart, label, color, data){
	
		for(i=1; i < data.length; i++){
			chart.data.datasets.push({
			label: label[i],
			backgroundColor: color[i],
			data: data[i],
			fill: false,
			borderColor: color[i]
			})};
	chart.update();
}

addData(myChart, column, colours , temp);

}


	