
// Create an object to store loaded images
const loadedImages = {};

function drawFromEvent(event, ctx) {
    const eventJSON = JSON.parse(event.data);

    for (const message of eventJSON) {
        const name = message.name;
        const parameterList = message.parameters;
        const type = message.type;

        if (type === "function") {
            if (name === "drawImage") {
                const imagePath = "/assets/" + parameterList[0];

                // Check if the image is already loaded
                if (loadedImages[imagePath]) {
                    parameterList[0] = loadedImages[imagePath];
                    ctx[name].apply(ctx, parameterList);
                } else {
                    const img = new Image();
                    img.src = imagePath;
                    img.onload = function() {
                        loadedImages[imagePath] = img; // Save the loaded image
                        ctx[name].apply(ctx, parameterList);
                    };
                }
            } else {
                ctx[name].apply(ctx, parameterList);
            }
        } else {
            ctx[name] = parameterList[0];
        }
    }
}

