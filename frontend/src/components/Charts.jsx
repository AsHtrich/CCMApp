import React, { useEffect, useState } from 'react';
import Chart from 'chart.js/auto';
import axios from 'axios';
const Charts = () => {
  const [tempChart, setTempChart] = useState(null);
  const [humidityChart, setHumidityChart] = useState(null);
  const [pressureChart, setPressureChart] = useState(null);

  useEffect(() => {
    function updateCharts() {
      // Fetch new data for temperature, humidity, and pressure
      axios.get('https://api.thingspeak.com/channels/2309020/fields/1.json?api_key=I2TWU0ISG1JNAJDI&results=1')
        .then((response) => {
          const data = response.data.feeds[0];
          const timestampUTC = new Date(data.created_at);
          const istOptions = { timeZone: 'Asia/Kolkata' , hour12: false};
          const timestamp = timestampUTC.toLocaleTimeString('en-US', istOptions);

          const temperature = parseFloat(data.field1);


          // Update temperature chart
          if (tempChart) {
            tempChart.data.labels.push(timestamp);
            tempChart.data.datasets[0].data.push(temperature);

            // Remove the oldest entry if the number of entries exceeds 5
            if (tempChart.data.labels.length > 5) {
              tempChart.data.labels.shift();
              tempChart.data.datasets[0].data.shift();
            }

            tempChart.update();
          }
        })
        .catch((error) => {
          console.error('Error fetching temperature data:', error);
        });

      axios.get('https://api.thingspeak.com/channels/2309020/fields/2.json?api_key=I2TWU0ISG1JNAJDI&results=1')
        .then((response) => {
          const data = response.data.feeds[0];
          const timestampUTC = new Date(data.created_at);
          const istOptions = { timeZone: 'Asia/Kolkata' , hour12: false};
          const timestamp = timestampUTC.toLocaleTimeString('en-US', istOptions);

          const humidity = parseFloat(data.field2);

          // Update humidity chart
          if (humidityChart) {
            humidityChart.data.labels.push(timestamp);
            humidityChart.data.datasets[0].data.push(humidity);

            // Remove the oldest entry if the number of entries exceeds 5
            if (humidityChart.data.labels.length > 5) {
              humidityChart.data.labels.shift();
              humidityChart.data.datasets[0].data.shift();
            }

            humidityChart.update();
          }
        })
        .catch((error) => {
          console.error('Error fetching humidity data:', error);
        });

      axios.get('https://api.thingspeak.com/channels/2309020/fields/3.json?api_key=I2TWU0ISG1JNAJDI&results=1')
        .then((response) => {
          const data = response.data.feeds[0];
          const timestampUTC = new Date(data.created_at);
          const istOptions = { timeZone: 'Asia/Kolkata' , hour12: false};
          const timestamp = timestampUTC.toLocaleTimeString('en-US', istOptions);

          const pressure = parseFloat(data.field3);

          // Update pressure chart
          if (pressureChart) {
            pressureChart.data.labels.push(timestamp);
            pressureChart.data.datasets[0].data.push(pressure);

            // Remove the oldest entry if the number of entries exceeds 5
            if (pressureChart.data.labels.length > 5) {
              pressureChart.data.labels.shift();
              pressureChart.data.datasets[0].data.shift();
            }

            pressureChart.update();
          }
        })
        .catch((error) => {
          console.error('Error fetching pressure data:', error);
        });
    }

    // Create an initial empty chart for temperature
    var tempCtx = document.getElementById('myChart1').getContext('2d');
    var tempChart = new Chart(tempCtx, {
      type: 'line',
      data: {
        labels: [],
        datasets: [
          {
            label: 'Temperature',
            data: [],
            borderColor: '#84bd00',
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        title: {
          display: true,
          text: 'Temperature Chart',
        },
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Time',
            },
            ticks: {
              maxTicksLimit: 5, // Set the maximum number of x-axis ticks
            },
          },
          y: {
            min: 25, // Set the minimum y-axis value to 70
            max: 36, // Set the maximum y-axis value to 100
            beginAtZero: false, // You may want to set this to false to explicitly start from 70
          },
        },
      },
    });
    

    // Create an initial empty chart for humidity
    var humidityCtx = document.getElementById('myChart2').getContext('2d');
    var humidityChart = new Chart(humidityCtx, {
      type: 'line',
      data: {
        labels: [],
        datasets: [
          {
            label: 'Humidity',
            data: [],
            borderColor: '#00205b',
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        title: {
          display: true,
          text: 'Humidity Chart',
        },
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Time',
            },
            ticks: {
              maxTicksLimit: 5, // Set the maximum number of x-axis ticks
            },
          },
          y: {
            beginAtZero: true,
          },
        },
      },
    });

    // Create an initial empty chart for pressure
    var pressureCtx = document.getElementById('myChart3').getContext('2d');
    var pressureChart = new Chart(pressureCtx, {
      type: 'line',
      data: {
        labels: [],
        datasets: [
          {
            label: 'Pressure',
            data: [],
            borderColor: '#ff0000',
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        title: {
          display: true,
          text: 'Pressure Chart',
        },
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Time',
            },
            ticks: {
              maxTicksLimit: 5, // Set the maximum number of x-axis ticks
            },
          },
          y: {
            beginAtZero: true,
          },
        },
      },
    });

    // Set the initial chart instances
    setTempChart(tempChart);
    setHumidityChart(humidityChart);
    setPressureChart(pressureChart);

    // Update charts periodically
    const updateInterval = setInterval(updateCharts, 30000); // Update every 30 seconds

    // Clean up the interval when the component unmounts
    return () => {
      clearInterval(updateInterval);
    };
  }, []);

  return (
    <div className='w-full flex-1 h-screen overflow-y-auto bg-white'>
      
      <div className='w-1/3 bg-white'>
        <canvas id='myChart1'></canvas>
      </div>
      <div className='w-1/3'>
        <canvas id='myChart2'></canvas>
      </div>
      <div className='w-1/3'>
        <canvas id='myChart3'></canvas>
      </div>
    </div>
  );
};

export default Charts;
