"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var FissionUpdater = (function () {
    function FissionUpdater(id) {
        this.clientId = id;
    }
    return FissionUpdater;
}());
// export const new FissionUpdater() : Updater
function print(msg) {
    console.log("[Printing]", msg);
}
exports.print = print;
