window.initMap = function () {
  const location = { lat: -33.0336892, lng: -71.5331841 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 16,
    center: location,
    restriction: {
      latLngBounds: {
        north: -33.0236892,
        south: -33.0436892,
        east: -71.5231841,
        west: -71.5431841,
      },
      strictBounds: true,
    },
    streetViewControl: false, // Disable Street View
  });
  new google.maps.Marker({
    position: location,
    map: map,
  });
};