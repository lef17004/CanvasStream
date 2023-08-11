function interpretMessage(messages) {
    for (const message of messages) {
        const type = message.type;
        const name = message.name;
        const parameters = message.parameters;

        if (type == "function") {
            ctx[name].apply(ctx, parameters);
        } else if (type == "variable") {
            ctx[name] = parameters[0];
        } else if (type == "command") {

        }
    }
}