
function drawFromEvent(event, ctx) {
    const eventJSON = JSON.parse(event.data);

    for (const message of eventJSON) {
        const name = message.name;
        const parameterList = message.parameters;
        const type = message.type;
    
        if (type === "function") {
            ctx[name].apply(ctx, parameterList);
        }
        else {
            ctx[name] = parameterList[0];
        }
        
    }
};