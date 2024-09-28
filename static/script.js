document.addEventListener("DOMContentLoaded", function () {
    // Connect to the Flask WebSocket server
    const socket = io();

    // Listen for stock updates from the server
    socket.on('stock_update', function (data) {
        console.log("Received live stock update:", data);

        // Update HTML elements with new stock data
        document.getElementById("stock-ticker").textContent = `Ticker: ${data.ticker}`;
        document.getElementById("stock-price").textContent = `Price: $${data.price}`;
        document.getElementById("stock-volume").textContent = `Volume: ${data.volume}`;
    });
});
