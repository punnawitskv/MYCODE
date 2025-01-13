let colorIndex = 0;
const colorPairs = [
    { textColor: "red", bgColor: "green" },
    { textColor: "purple", bgColor: "yellow" },
    { textColor: "blue", bgColor: "orange" },
    { textColor: "green", bgColor: "red" },
    { textColor: "yellow", bgColor: "purple" },
    { textColor: "orange", bgColor: "blue" }
];

function updateDateTime() {
    const now = new Date();
    const currentColorPair = colorPairs[colorIndex];
    colorIndex = (colorIndex + 1) % colorPairs.length;

    postMessage({
        dateTime: now.toString(),
        color: currentColorPair
    });
}

onmessage = function (e) {
    if (e.data === 'start') {
        updateDateTime();
    }
};

setInterval(updateDateTime, 1000);
