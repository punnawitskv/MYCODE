// worker.js
const colorPairs = [
    { textColor: "red", bgColor: "green" },
    { textColor: "purple", bgColor: "yellow" },
    { textColor: "blue", bgColor: "orange" },
    { textColor: "green", bgColor: "red" },
    { textColor: "yellow", bgColor: "purple" },
    { textColor: "orange", bgColor: "blue" }
];

let colorIndex = 0;

updateDateTime()

function updateDateTime() {
    const now = new Date();
    const currentColorPair = colorPairs[colorIndex];
    colorIndex = (colorIndex + 1) % colorPairs.length;

    return {
        time: now.toString(),
        textColor: currentColorPair.textColor,
        bgColor: currentColorPair.bgColor
    };
}

// Listen for messages from the main thread
self.onmessage = function () {
    const dateTime = updateDateTime();
    postMessage(dateTime);  // Send data back to the main thread
};

// Set an interval to send updates every second
setInterval(() => {
    self.postMessage(updateDateTime());
}, 1000);
