document.addEventListener('DOMContentLoaded', function () {
    fetchData();
});

function fetchData() {
    fetch('http://127.0.0.1:8000/store/products/')
        .then(response => response.json())
        .then(data => {
            console.log('API Response:', data);
            updateUI(data);
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('item-container').innerText = 'Error fetching data';
        });
}

function updateUI(data) {
    console.log('Updating UI with data:', data);

    // Reference to the container where you want to display the items
    var container = document.getElementById('item-container');

    // Clear existing content in the container
    container.innerHTML = '';

    // Check if there is at least one item in the array
    if (data && data.length > 0) {
        // Iterate through the array and create HTML elements for each item
        data.forEach(item => {
            var itemElement = document.createElement('div');
            itemElement.className = 'item';

            // Fetch a food-related image from Unsplash
            fetch(`https://source.unsplash.com/200x200/?food`)
                .then(response => {
                    // Create an image element with the fetched URL
                    var imageElement = document.createElement('img');
                    imageElement.src = response.url;
                    imageElement.alt = 'Food Image';

                    // Append image to the item container
                    itemElement.appendChild(imageElement);
                })
                .catch(error => {
                    console.error('Error fetching food image:', error);
                });

            var titleElement = document.createElement('h2');
            titleElement.innerText = item.title || 'Title not available';

            var descriptionElement = document.createElement('p');
            descriptionElement.innerText = item.description || 'Description not available';

            // Append title and description to the item container
            itemElement.appendChild(titleElement);
            itemElement.appendChild(descriptionElement);

            // Append the item container to the main container
            container.appendChild(itemElement);
        });
    } else {
        // Handle the case when the array is empty
        var noDataElement = document.createElement('p');
        noDataElement.innerText = 'No data available';
        container.appendChild(noDataElement);
    }
}
