function solution(new_id) {
    new_id = new_id.toLowerCase()
        .replace(/[^a-z0-9-_.]/g,"")
        .replace(/\.+/g,".")
        .replace(/^\.|\.$/g,"")
        .slice(0,15).replace(/\.$/,"");
    if (new_id.length === 0) new_id = "a";
    const diff = 3 - new_id.length;
    if (new_id.length <= 2) {
         new_id = new_id + new_id.substr(-1).repeat(diff);
    }
    return new_id;
}
