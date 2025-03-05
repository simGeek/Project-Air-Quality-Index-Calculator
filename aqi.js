// Add a click event listener to the submit button with ID "submitAqi"
document.getElementById("submitAqi").addEventListener("click", function(event) {
    // Retrieve values from input fields by their IDs
    var input1Value = document.getElementById("pm2dot5").value; // PM2.5 value
    var input2Value = document.getElementById("pm10").value; // PM10 value
    var input3Value = document.getElementById("no2").value; // NO2 value
    var input4Value = document.getElementById("nox").value; // NOx value
    var input5Value = document.getElementById("nh3").value; // NH3 value
    var input6Value = document.getElementById("co").value; // CO value
    const form = document.getElementById('form_id'); // Get the form element

    // Check if any input fields are empty
    if (
        input1Value.trim() === "" || input2Value.trim() === "" ||
        input3Value.trim() === "" || input4Value.trim() === "" || 
        input5Value.trim() === "" || input6Value.trim() === "" 
    ) {
        // Alert the user to fill in all fields
        alert("Please enter values in all input fields.");
        event.preventDefault(); // Prevent form submission
    }
    else {
        // Log to console that all fields are filled
        console.log("All input fields have values. Submitting...");
        
        // Create a FormData object from the form
        const formData = new FormData(form);

        // Send a POST request to the server at 'p2_regression/'
        fetch('/aqi_regression/', {
            method: 'POST', // Set the request method to POST
            body: formData // Attach the form data to the request
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            // Store the predictions in local storage
            localStorage.setItem('aqiPredictions', JSON.stringify(data.predictions));
        })
        .catch(error => {
            // Log any errors that occur during the fetch
            console.error('Error:', error);
        })
   }
});
