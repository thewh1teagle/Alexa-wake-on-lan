const WebSocket = require('ws');
var wol = require('wake_on_lan');



var pc_mac = 'aa:bb:cc:dd:ee:ff' // Change for your pc mac
var device_id = "" // Grab it from sinric.com
const token = ""; // Grab it from sinric.com


const options = {
    headers: {
        "Authorization" : Buffer.from("apikey:" + token).toString('base64')
    }
};

 // Keep live and detect disconnection
 function heartbeat() {
    clearTimeout(this.pingTimeout);
  
    this.pingTimeout = setTimeout(() => {
      console.log("No Connection. Killing node...")
      this.terminate();
    }, 30000 + 1000);
  }

const ws = new WebSocket('ws://iot.sinric.com', options);

ws.on('open', heartbeat);
ws.on('ping', heartbeat);
ws.on('close', function clear() {
  clearTimeout(this.pingTimeout);
});

ws.on('open', function open() {
   console.log("Connected. waiting for commands..");
});

ws.on('message', function incoming(data) {
   console.log("Request : " + data)
   let cmdObj = JSON.parse(data);
   if(cmdObj.deviceId == device_id) {
	   if(cmdObj.action == "setPowerState") {
       	if(cmdObj.value === "ON") {
        	    wol.wake(pc_mac);
	            console.log("Turn on...")
	       }
	   }
   }
});
