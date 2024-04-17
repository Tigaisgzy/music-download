function f() {
    var guid = (new Date).getUTCMilliseconds();
    guid = String(Math.round(2147483647 * Math.random()) * guid % 1e10);
    console.log(guid)
    return guid;
}


