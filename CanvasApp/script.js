let imageCache = {};

var canvas = document.getElementById("myCanvas");
let ctx = canvas.getContext("2d");


ctx.drawImg = function(imagePath, dx, dy, dWidth = null, dHeight = null) {

    if (!(imagePath in imageCache)) {
        const newImage = new Image();
        newImage.src = "/assets/" + imagePath;
        imageCache[imagePath] = newImage;
    }
    
    let args = [imageCache[imagePath], dx, dy];
    if (dWidth != null && dHeight != null) {
        args.push(dWidth);
        args.push(dHeight);
    }

    // Call the original drawImage method
    ctx.drawImage.apply(ctx, args);
};


let socket = new WebsocketConection();