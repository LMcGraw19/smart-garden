function startup(time, temp, humi) {
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
}




function BME280(time, temp, pres, alti, humi) {

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
	    type: 'line',
        data: {
            labels: time,
            datasets: [{
			    label: 'Temperture',
                data: temp,
                
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
            },
			{label: 'Humidity',
			type: 'line',
                data: humi,
                
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
        },
		{label: 'Approx. altitud',
			type: 'line',
                data: alti,
                
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
        },
		{label: 'Barometric pressure',
			type: 'line',
                data: pres,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
        }]
		
		},
        options: {layout: {
            padding: {
                left: 0,
                right: 4,
                top: 0,
                bottom: 0
            }
        },
			scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            
        },
		maintainAspectRatio: false
		}
    })
};




function DS18B20(time, temp) {

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
	    type: 'line',
        data: {
            labels: time,
            datasets: [{
			    label: 'Temperture',
                data: temp,
                
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
            },]
		
		},
        options: {layout: {
            padding: {
                left: 0,
                right: 4,
                top: 0,
                bottom: 0
            }
        },
			scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            
        },
		maintainAspectRatio: false
		}
    })
};

function SEN0114(time, mois) {

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
	    type: 'line',
        data: {
            labels: time,
            datasets: [{
			    label: 'Moisture',
                data: mois,
                
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
            },
			]
		
		},
        options: {layout: {
            padding: {
                left: 0,
                right: 4,
                top: 0,
                bottom: 0
            }
        },
			scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            
        },
		maintainAspectRatio: false
		}
    })
};

function SHT21(time, temp, humi) {

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
	    type: 'line',
        data: {
            labels: time,
            datasets: [{
			    label: 'Temperture',
                data: temp,
                
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
            },
			{label: 'Humidity',
			type: 'line',
                data: humi,
                
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
        }]
		
		},
        options: {layout: {
            padding: {
                left: 0,
                right: 4,
                top: 0,
                bottom: 0
            }
        },
			scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            
        },
		maintainAspectRatio: false
		}
    })
};

function TSL2591(time, lumi) {

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
	    type: 'line',
        data: {
            labels: time,
            datasets: [{
			    label: 'Luminosity',
                data: lumi,
                
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
				fill: false
            }]
		
		},
        options: {layout: {
            padding: {
                left: 0,
                right: 4,
                top: 0,
                bottom: 0
            }
        },
			scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            
        },
		maintainAspectRatio: false
		}
    })
};


	