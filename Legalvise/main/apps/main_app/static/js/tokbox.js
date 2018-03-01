// replace these values with those generated in your TokBox Account
var apiKey = "46070162";
var sessionId = "1_MX40NjA3MDE2Mn5-MTUxOTg3MjkwNjk5Nn5vcE5EczI5RlZ2Q2tra2lBbXZ0NVEyMGl-fg";
var token = "T1==cGFydG5lcl9pZD00NjA3MDE2MiZzaWc9ZjliNDQxZmNmYzdhYjY5NzkzYTNlZDllNDU4MzQwMDY0MmE5ZThlNDpzZXNzaW9uX2lkPTFfTVg0ME5qQTNNREUyTW41LU1UVXhPVGczTWprd05qazVObjV2Y0U1RWN6STVSbFoyUTJ0cmEybEJiWFowTlZFeU1HbC1mZyZjcmVhdGVfdGltZT0xNTE5OTIzNTU5Jm5vbmNlPTAuNjk0NjUwNDc5MTQyMDUwNSZyb2xlPXB1Ymxpc2hlciZleHBpcmVfdGltZT0xNTE5OTQ1MTU4JmluaXRpYWxfbGF5b3V0X2NsYXNzX2xpc3Q9";

// (optional) add server code here
initializeSession();

// Handling all of our errors here by alerting them
function handleError(error) {
    if (error) {
      alert(error.message);
    }
  }

function initializeSession() {
var session = OT.initSession(apiKey, sessionId);

// Subscribe to a newly created stream
session.on('streamCreated', function(event) {
    session.subscribe(event.stream, 'subscriber', {
        insertMode: 'append',
        width: '100%',
        height: '100%'
    }, handleError);
    });

// Create a publisher
var publisher = OT.initPublisher('publisher', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
}, handleError);

// Connect to the session
session.connect(token, function(error) {
    // If the connection is successful, publish to the session
    if (error) {
    handleError(error);
    } else {
    session.publish(publisher, handleError);
    }
});
}