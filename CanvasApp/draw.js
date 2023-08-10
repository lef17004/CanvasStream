
function drawFromEvent(event, ctx) {
    const eventJSON = JSON.parse(event.data);

    for (const message of eventJSON) {
        const name = message.name;
        const parameterList = message.parameters;
        const type = message.type;
    
        if (type === "function") {
            if (name == "drawImage") {
                var img = new Image();      // First create the image...
                img.src = "/assets/" + parameterList[0];
                parameterList[0] = img;
                img.onload = function(){  // ...then set the onload handler...
                    ctx[name].apply(ctx, parameterList);
                };
                
            }
            
            ctx[name].apply(ctx, parameterList);
            
            
            
        }
        else {
            ctx[name] = parameterList[0];
        }
        
    }
};