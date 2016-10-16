var map = new GMaps({
  div: '#map',
  lat: 18.2208,
  lng: -66.5901,
  zoom: 10
});

function classify(int) {
	if (int <= 1.0) {
		return {rate: 'Poor', color: 'red'};
	} else if (int >= 1.0 & int <= 2.0) {
		return {rate: 'Poor-Medium', color: '#ff3300'};
	} else if (int >= 2.1 & int <= 3.0) {
		return {rate: 'Average', color: '#ffff00'};
	} else if (int >= 3.1 & int < 4.0) {
		return {rate: 'Average-High', color: '#ffcc00'};
	} else if (int >= 4.0) {
		return {rate: 'Excellent', color: '#00cc00'};
	}
}

var App = {
	base_url: "http://127.0.0.1:5000/v1",
	init: function () {

	},
	url: function (path) {
		return App.base_url + path;
	},
	getDataset: function (params, callback) {
		$.getJSON(App.url('/municipalities?municipality=') + municipality).done(callback);
	},
	addMarkersFromDataset: function (set) {
		_.each(set, function (item) {
			var lat = item.location_1.latitude;
			var long = item.location_1.longitude;
			if (!lat || !long) {
				console.log(item)
			} else {
				map.addMarker({
					lat: lat,
					lng: long,
					infoWindow: {
						content: '<a href="m/' + item.location_1.human_address.city + '">' + "<i>Graduate</i><br>GPA: " + item.gpa + '</a>'
					}
				});
				console.log(item.gpa);

				if (item.gpa) {
					c = classify(item.gpa);
				} else {
					var c = {color: "red"}
				}
				if (c) {
					console.log(c.color);
					map.drawCircle({
						lat: lat,
						lng: long,
						radius: 5000,
						fillOpacity: 0.1,
						fillColor: c.color,
						strokeWeight: 0.0001						
					})
				}
			}
			var sei = false;

			if (sei) {
				// add circle marker for the S.E.I.
				map.drawCircle({
					lat: lat,
					lng: long,
					radius: 5000,
					fillOpacity: 0.1,
					fillColor: 'green',
					strokeWeight: 0.0001						
				})
			}
		})
	},
	markerClick: function (i) {
		console.log("Opening" + i.codigo);
		window.open("school/" + i.codigo, "_self");
	}
}



$(document).ready(function () {

	App.getDataset({

	}, App.addMarkersFromDataset);
})

