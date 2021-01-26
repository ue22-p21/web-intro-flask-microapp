"use strict"

let COLOR = "pink"

function armMouseFollower(image_id, x_id, y_id, area_id) {
    let elt = document.getElementById(image_id);
    // preserve color
    let color = document.body.style.backgroundColor;
    let [x1, y1] = [0, 0];

    let isMouseDown = false;
    elt.onmousedown = function (event) {
        // remove default behaviour which is to drag image
        event.preventDefault();
        document.body.style.backgroundColor = COLOR;
        isMouseDown = true;
        [x1, y1] = showCoordinates(event, image_id, x_id, y_id);
    }
    elt.onmouseup = function (event) {
        event.preventDefault();
        document.body.style.backgroundColor = color;
        isMouseDown = false;
        showArea(event, image_id, area_id, x1, y1);
    }
    elt.onmousemove = function (event) {
        event.preventDefault();
        if (isMouseDown) {
            showCoordinates(event, image_id, x_id, y_id);
        }
    }
 }

// position of the element inside the document
function relativePosition(elt) {
    if (typeof (elt.offsetParent) != "undefined") {
        let pos_x = 0;
        let pos_y = 0;
        for (; elt; elt = elt.offsetParent) {
            pos_x += elt.offsetLeft;
            pos_y += elt.offsetTop;
        }
        return [pos_x, pos_y];
    } else {
        return [elt.x, elt.y];
    }
 }

// compute mouse coordinates relative to a DOM elt
function getRelativeMouse(event, image_id) {
    let elt = document.getElementById(image_id);
    let [rel_x, rel_y] = relativePosition(elt);

    let pos_x = 0;
    let pos_y = 0;
    if (!event) event = window.event;
    if (event.pageX || event.pageY) {
        pos_x = event.pageX;
        pos_y = event.pageY;
    } else if (event.clientX || event.clientY) {
        pos_x = event.clientX + document.body.scrollLeft
            + document.documentElement.scrollLeft;
        pos_y = event.clientY + document.body.scrollTop
            + document.documentElement.scrollTop;
    }
    return [pos_x - rel_x, pos_y - rel_y];
 }

// like getRelativeMouse, but displays result
// in the x_id and y_id DOM elements
function showCoordinates(event, image_id, x_id, y_id) {
    let [pos_x, pos_y] = getRelativeMouse(event, image_id);
    document.getElementById(x_id).innerHTML = pos_x;
    document.getElementById(y_id).innerHTML = pos_y;
    return [pos_x, pos_y];
}

// computes current mouse position, and
// sends back to server a request to compute area
// wrt the (x1, y1) initial point
// the result is displayed in the aread_id DOM element
function showArea(event, image_id, area_id, x1, y1) {
    let [x2, y2] = getRelativeMouse(event, image_id);

    // post a GET request back to the same server
    const http = new XMLHttpRequest();
    const url=`/api/image/area/${image_id}/${x1}/${y1}/${x2}/${y2}`;
    http.open("GET", url);
    http.send();

    // how to behave when the answer comes back
    http.onreadystatechange = (event) => {
        // the answer is a JSON encoded Python dict
        let response = JSON.parse(http.responseText);
        // which results in a JavaScript regular object
        // that has the 'area' property
        document.getElementById(area_id).innerHTML = response.area;
    }
}
