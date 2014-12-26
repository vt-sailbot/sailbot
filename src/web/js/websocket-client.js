window.onload = function() {

	socket = new WebSocket('ws://127.0.0.1:8888/ws');

	socket.onmessage = function(s) {
		
		data = JSON.parse(s.data);
		
		document.getElementById("timestamp").innerHTML = data.timestamp;
		
		document.getElementById("lat").innerHTML = data.lat;
		document.getElementById("long").innerHTML = data.long;
		
		document.getElementById("target_lat").innerHTML = data.target_lat;
		document.getElementById("target_long").innerHTML = data.target_long;
		
		document.getElementById("heading").innerHTML = data.heading;
		document.getElementById("speed").innerHTML = data.speed;
		document.getElementById("wind_dir").innerHTML = data.wind_dir;
		document.getElementById("roll").innerHTML = data.roll;
		document.getElementById("pitch").innerHTML = data.pitch;
		document.getElementById("yaw").innerHTML = data.yaw;
		
		document.getElementById("state").innerHTML = data.state;
		
		update_boat_marker(data.lat, data.long);

	};

}