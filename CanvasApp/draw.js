
function drawFromEvent(event, ctx) {
    const eventJSON = JSON.parse(event.data);

    for (const message of eventJSON) {
        const functionToCall = message.function;
        const parameterList = message.parameters;
    
        switch (functionToCall) {
            case "beginPath":
                ctx.beginPath();
                break;
            case "lineWidth":
                ctx.lineWidth = parameterList[0];
                break;
            case "strokeStyle":
                ctx.strokeStyle = parameterList[0];
                break;
            case "rect":
                ctx.rect(parameterList[0],parameterList[1],parameterList[2],parameterList[3]);
                break;
            case "stroke":
                if (parameterList.length === 0){
                    ctx.stroke();
                }
                else {
                    ctx.stroke(parameterList[0]);
                }
                break;
            case "arc":
                ctx.arc(parameterList[0],parameterList[1],parameterList[2],parameterList[3],parameterList[4]);
                break;
            case "fillStyle":
                ctx.fillStyle = parameterList[0];
                break;
            case "fill":
                ctx.fill();
        }
    }
};