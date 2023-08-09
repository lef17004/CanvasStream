
function drawFromEvent(event, ctx) {
    const eventJSON = JSON.parse(event.data);

    const functionToCall = eventJSON.function;
    const parameterList = eventJSON.parameters;

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
            ctx.rect(parameterList[0],parameterList[1],parameterList[2],parameterList[3])
            break;
        case "stroke":
            if (parameterList.length === 0){
                ctx.stroke();
            }
            else {
                ctx.stroke(parameterList[0]);
            }
            break;
    }
};