document.getElementById('loadData').addEventListener('click', function() {
    fetch('/data')
    .then(response => response.json())
    .then(data => {
        document.getElementById('data').textContent = data.message;
    });
});
